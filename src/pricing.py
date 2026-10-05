"""
Token pricing for cost estimation — USD per 1M tokens (input, output), keyed by
the full "provider:model" id recorded in the roster (see llm.model_id).

Gemini on the FREE tier costs $0 (rate-limited instead). If you move to a paid
Gemini key, set GEMINI_PAID=1 so the README spend estimate uses paid rates.
Stdlib-only so the stats/README generator can import it without SDKs.
"""
import os

# Fill in from https://ai.google.dev/pricing if you ever switch to a paid key.
_GEMINI_PAID = {
    # "gemini:gemini-3.8-flash": (input $/1M, output $/1M),
}

PRICES = {
    "anthropic:claude-opus-5-5":   (4.0, 20.0),
    "anthropic:claude-sonnet-5-5": (2.0, 10.0),
    "anthropic:claude-haiku-4-5":  (1.0, 5.0),
}
if os.environ.get("GEMINI_PAID", "").strip() in ("1", "true", "yes"):
    PRICES.update(_GEMINI_PAID)


def _int(v):
    try:
        return int(v)
    except (TypeError, ValueError):
        return 0


def cost_usd(model_id, tok_in, tok_out):
    """Estimated USD for a call. Free-tier / unknown models cost 0."""
    p_in, p_out = PRICES.get(model_id or "", (0.0, 0.0))
    return _int(tok_in) / 1e6 * p_in + _int(tok_out) / 1e6 * p_out
