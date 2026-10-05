"""
The ONE place the pipeline talks to an LLM. Everything else (eligibility,
extraction) builds a list of provider-neutral `parts` + a Pydantic schema and
calls `llm.call(...)`. Swapping provider = changing a model spec string.

Model specs
-----------
A spec is "provider:model-id", a comma-separated FAILOVER CHAIN of them, or a
short alias from ALIASES:

    flash   -> gemini-3.8-flash, then 3.5-flash, 3.7-flash, 3.1-flash-lite
               (default for eligibility; Google free tier — see "Rate limits")
    flash-extract -> the same without flash-lite (default for extraction)
    pro     -> gemini:gemini-pro-latest, then the flash chain
    opus    -> anthropic:claude-opus-5-5
    sonnet  -> anthropic:claude-sonnet-5-5
    haiku   -> anthropic:claude-haiku-4-5
    gpt     -> openai:gpt-5

Any "provider:model" works without an alias, e.g. "gemini:gemini-3.5-flash".
List what your Gemini key can use with:  python src/llm.py --list-models

Providers and their env vars
----------------------------
    gemini     GEMINI_API_KEY      (pip: google-genai)
    anthropic  ANTHROPIC_API_KEY   (pip: anthropic)
    openai     OPENAI_API_KEY      (pip: openai). Set OPENAI_BASE_URL to point at
               any OpenAI-compatible server (OpenRouter, Mistral, a local model…);
               PDF input must be supported by that server.

To add another provider: write a `_call_<name>(model, system, parts, schema,
max_tokens)` that returns an `LLMResult`, and register it in BACKENDS.

Rate limits (free tier)
-----------------------
The Gemini free tier allows only ~20 requests/DAY per model (per project) and
models are often "busy" (503). So a call works down its chain:
  - daily quota used up (429, long retry delay) -> skip that model for the rest
    of this run, immediately — never wait hours;
  - busy / server error -> retry LLM_MAX_RETRIES times (default 2), then move on;
  - short rate limit (Google asks to wait <= 2 min) -> wait, then retry.
Calls are also spaced LLM_MIN_INTERVAL seconds apart (default 7 s for Gemini).
The model that actually answered is in LLMResult.model_id (and the roster).
"""
import base64
import os
import random
import re
import sys
import time
from dataclasses import dataclass, field

from pydantic import BaseModel, ValidationError

_FLASH_CHAIN = ("gemini:gemini-3.8-flash,gemini:gemini-3.5-flash,"
                "gemini:gemini-3.7-flash,gemini:gemini-3.1-flash-lite")
# Extraction needs the stronger models: same chain without flash-lite.
_EXTRACT_CHAIN = _FLASH_CHAIN.rsplit(",", 1)[0]
ALIASES = {
    "flash": _FLASH_CHAIN,
    "flash-extract": _EXTRACT_CHAIN,
    "pro": "gemini:gemini-pro-latest," + _FLASH_CHAIN,
    "opus": "anthropic:claude-opus-5-5",
    "sonnet": "anthropic:claude-sonnet-5-5",
    "haiku": "anthropic:claude-haiku-4-5",
    "gpt": "openai:gpt-5",
}
DEFAULT_MODEL = "flash"

# Models whose output limit is below what callers may ask for (others accept 64K+).
MAX_OUTPUT = {"claude-haiku-4-5": 64000}

def _load_dotenv():
    """Read KEY=value lines from the project's .env file (git-ignored) into the
    environment, without overriding variables that are already set."""
    from pathlib import Path
    path = Path(__file__).resolve().parent.parent / ".env"
    if not path.exists():
        return
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip().removeprefix("export ").strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))


_load_dotenv()

MAX_RETRIES = int(os.environ.get("LLM_MAX_RETRIES", "2"))   # per model, before failing over
MAX_WAIT = 120          # never sleep longer than this; longer = quota exhausted, fail over
DEFAULT_INTERVAL = {"gemini": 7.0}   # seconds between calls, per provider


# --- Provider-neutral inputs and output ------------------------------------

@dataclass
class Pdf:
    data: bytes
    name: str = "paper.pdf"


@dataclass
class Text:
    text: str


@dataclass
class LLMResult:
    parsed: BaseModel | None       # validated schema instance, or None
    stop_reason: str               # "end" | "max_tokens" | "refusal" | provider-specific
    tok_in: int = 0
    tok_out: int = 0
    model_id: str = ""             # "provider:model" actually used
    raw_text: str = ""             # for debugging when parsing fails
    error: str = ""                # parse/validation error, if any
    extra: dict = field(default_factory=dict)


def resolve(spec):
    """'flash' -> [('gemini', 'gemini-3.8-flash'), ('gemini', 'gemini-3.5-flash'), ...]."""
    spec = spec or DEFAULT_MODEL
    spec = ALIASES.get(spec, spec)
    chain = []
    for item in spec.split(","):
        item = ALIASES.get(item.strip(), item.strip())
        if "," in item:                      # an alias inside a chain
            chain.extend(resolve(item))
            continue
        if ":" not in item:
            sys.exit(f"Model spec '{item}' must be an alias ({', '.join(ALIASES)}) or 'provider:model'.")
        provider, model = item.split(":", 1)
        if provider not in BACKENDS:
            sys.exit(f"Unknown provider '{provider}'. Known: {', '.join(BACKENDS)}.")
        chain.append((provider, model))
    return chain


def model_id(spec):
    """'provider:model' of the FIRST model in the chain (for display)."""
    p, m = resolve(spec)[0]
    return f"{p}:{m}"


# --- Throttle + retry + failover ---------------------------------------------

_last_call = {}
_exhausted = {}        # "provider:model" -> reason, for the rest of this process


class AllModelsFailed(RuntimeError):
    pass


def _throttle(provider):
    interval = float(os.environ.get("LLM_MIN_INTERVAL", DEFAULT_INTERVAL.get(provider, 0.0)))
    wait = _last_call.get(provider, 0.0) + interval - time.monotonic()
    if wait > 0:
        time.sleep(wait)
    _last_call[provider] = time.monotonic()


def _status(exc):
    return (getattr(exc, "code", None) or getattr(exc, "status_code", None)
            or getattr(getattr(exc, "response", None), "status_code", None))


def _classify(exc):
    """-> ('quota' | 'wait' | 'busy' | 'fatal', delay_seconds or None)."""
    status, text, name = _status(exc), str(exc), type(exc).__name__
    delay = None
    m = re.search(r"retryDelay['\"]?\s*[:=]\s*['\"]?(\d+(?:\.\d+)?)s", text) \
        or re.search(r"retry in (\d+(?:\.\d+)?)s", text)
    if m:
        delay = float(m.group(1))
    if status == 429:
        if "PerDay" in text or (delay is not None and delay > MAX_WAIT):
            return "quota", delay
        return "wait", delay
    if status == 404:                       # model retired / not available to this key
        return "quota", None
    if isinstance(status, int) and (status >= 500 or status == 408):
        return "busy", delay
    if "Connection" in name or "Timeout" in name:
        return "busy", None
    return "fatal", None


def _fmt_hours(sec):
    return f"{sec / 3600:.1f} h" if sec else "unknown time"


def call(spec, system, parts, schema, max_tokens=16000):
    """Send `parts` (list of Pdf/Text) with a system prompt; return an LLMResult
    whose `.parsed` is an instance of `schema` (or None if the model refused,
    was truncated, or returned invalid JSON — see .stop_reason / .error).

    Works down the model chain (see module docstring); raises AllModelsFailed if
    every model is out of quota or keeps failing."""
    chain = resolve(spec)
    notes = []
    for provider, model in chain:
        mid = f"{provider}:{model}"
        if mid in _exhausted:
            notes.append(f"{mid}: {_exhausted[mid]}")
            continue
        fn = BACKENDS[provider]
        limit = min(max_tokens, MAX_OUTPUT.get(model, max_tokens))
        attempt = 0
        while True:
            _throttle(provider)
            try:
                res = fn(model, system, parts, schema, limit)
                res.model_id = mid
                return res
            except Exception as e:
                kind, delay = _classify(e)
                if kind == "fatal":
                    raise
                if kind == "quota":
                    reason = (f"daily quota used up (resets in {_fmt_hours(delay)})"
                              if _status(e) == 429 else f"not available ({_status(e)})")
                    _exhausted[mid] = reason
                    notes.append(f"{mid}: {reason}")
                    print(f"    (llm: {mid} {reason} — trying next model)")
                    break
                attempt += 1
                if attempt > MAX_RETRIES:
                    notes.append(f"{mid}: still {'busy' if kind == 'busy' else 'rate-limited'} "
                                 f"after {MAX_RETRIES} retries")
                    print(f"    (llm: {mid} still {kind} — trying next model)")
                    break
                delay = min(delay or (5 * 2 ** attempt + random.uniform(0, 3)), MAX_WAIT)
                why = "provider busy" if kind == "busy" else "rate limit"
                print(f"    (llm: {mid} {why}; retry {attempt}/{MAX_RETRIES} in {delay:.0f}s)")
                time.sleep(delay)
    raise AllModelsFailed("No model could answer:\n  " + "\n  ".join(notes)
                          + "\nWait for the quota to reset, try later, or pass another --model.")


def _validate(schema, text):
    """Parse model text into the schema; tolerate ```json fences."""
    t = (text or "").strip()
    if t.startswith("```"):
        t = re.sub(r"^```(?:json)?\s*|\s*```$", "", t)
    try:
        return schema.model_validate_json(t), ""
    except ValidationError as e:
        return None, f"schema validation failed: {e}"[:2000]


# --- Gemini (default) -------------------------------------------------------

_clients = {}


def _call_gemini(model, system, parts, schema, max_tokens):
    from google import genai
    from google.genai import types

    if "gemini" not in _clients:
        key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
        if not key:
            sys.exit("Set GEMINI_API_KEY.")
        _clients["gemini"] = genai.Client(api_key=key)
    client = _clients["gemini"]

    contents = []
    for p in parts:
        if isinstance(p, Pdf):
            contents.append(types.Part.from_bytes(data=p.data, mime_type="application/pdf"))
        else:
            contents.append(p.text)

    resp = client.models.generate_content(
        model=model,
        contents=contents,
        config=types.GenerateContentConfig(
            system_instruction=system,
            response_mime_type="application/json",
            response_json_schema=schema.model_json_schema(),
            max_output_tokens=max_tokens,
            temperature=0,
            automatic_function_calling=types.AutomaticFunctionCallingConfig(disable=True),
        ),
    )
    um = resp.usage_metadata
    tok_in = (um.prompt_token_count or 0) if um else 0
    tok_out = ((um.candidates_token_count or 0) + (um.thoughts_token_count or 0)) if um else 0

    cand = (resp.candidates or [None])[0]
    finish = str(getattr(cand, "finish_reason", "") or "").rsplit(".", 1)[-1]
    stop = {"STOP": "end", "MAX_TOKENS": "max_tokens", "SAFETY": "refusal",
            "PROHIBITED_CONTENT": "refusal", "RECITATION": "refusal"}.get(finish, finish.lower() or "unknown")
    if resp.prompt_feedback and getattr(resp.prompt_feedback, "block_reason", None):
        stop = "refusal"

    text = resp.text if stop == "end" else ""
    parsed, err = _validate(schema, text) if text else (None, f"no output (stop: {stop})")
    return LLMResult(parsed, stop, tok_in, tok_out, raw_text=text or "", error=err)


# --- Anthropic --------------------------------------------------------------

def _call_anthropic(model, system, parts, schema, max_tokens):
    import anthropic

    if "anthropic" not in _clients:
        _clients["anthropic"] = anthropic.Anthropic()
    client = _clients["anthropic"]

    content = []
    for p in parts:
        if isinstance(p, Pdf):
            content.append({"type": "document", "source": {
                "type": "base64", "media_type": "application/pdf",
                "data": base64.standard_b64encode(p.data).decode("utf-8")}})
        else:
            content.append({"type": "text", "text": p.text})

    # Streaming so large extractions don't hit the HTTP timeout.
    with client.messages.stream(
        model=model,
        max_tokens=max_tokens,
        system=system,
        messages=[{"role": "user", "content": content}],
        output_format=schema,
    ) as stream:
        resp = stream.get_final_message()

    stop = {"end_turn": "end"}.get(resp.stop_reason, resp.stop_reason)
    parsed = getattr(resp, "parsed_output", None)
    raw = "".join(b.text for b in resp.content if b.type == "text")
    err = "" if parsed is not None else f"no structured output (stop: {stop})"
    return LLMResult(parsed, stop, resp.usage.input_tokens, resp.usage.output_tokens,
                     raw_text=raw, error=err)


# --- OpenAI / OpenAI-compatible ---------------------------------------------

def _call_openai(model, system, parts, schema, max_tokens):
    import openai

    if "openai" not in _clients:
        _clients["openai"] = openai.OpenAI()   # honours OPENAI_API_KEY / OPENAI_BASE_URL
    client = _clients["openai"]

    content = []
    for p in parts:
        if isinstance(p, Pdf):
            b64 = base64.standard_b64encode(p.data).decode("utf-8")
            content.append({"type": "file", "file": {
                "filename": p.name, "file_data": f"data:application/pdf;base64,{b64}"}})
        else:
            content.append({"type": "text", "text": p.text})

    resp = client.chat.completions.parse(
        model=model,
        max_completion_tokens=max_tokens,
        messages=[{"role": "system", "content": system},
                  {"role": "user", "content": content}],
        response_format=schema,
    )
    choice = resp.choices[0]
    stop = {"stop": "end", "length": "max_tokens", "content_filter": "refusal"}.get(
        choice.finish_reason, choice.finish_reason)
    if getattr(choice.message, "refusal", None):
        stop = "refusal"
    parsed = choice.message.parsed
    u = resp.usage
    return LLMResult(parsed, stop, getattr(u, "prompt_tokens", 0), getattr(u, "completion_tokens", 0),
                     raw_text=choice.message.content or "",
                     error="" if parsed is not None else f"no structured output (stop: {stop})")


BACKENDS = {"gemini": _call_gemini, "anthropic": _call_anthropic, "openai": _call_openai}


if __name__ == "__main__":
    if "--list-models" in sys.argv:
        from google import genai
        c = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))
        for m in c.models.list():
            if "generateContent" in (getattr(m, "supported_actions", None) or []):
                print(m.name.removeprefix("models/"))
    else:
        print(__doc__)
