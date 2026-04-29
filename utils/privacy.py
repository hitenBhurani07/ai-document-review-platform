"""Privacy helpers for masking sensitive business data."""

from __future__ import annotations

import re


EMAIL_REPLACEMENT = "[REDACTED_EMAIL]"
PHONE_REPLACEMENT = "[REDACTED_PHONE]"
BANK_REPLACEMENT = "[REDACTED_BANK]"

EMAIL_PATTERN = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")
PHONE_PATTERN = re.compile(
    r"(?<!\w)(?:\+?\d{1,3}[\s.-]?)?(?:\(?\d{2,4}\)?[\s.-]?)\d{3,4}[\s.-]?\d{3,4}(?!\w)"
)
BANK_HINT_PATTERN = re.compile(
    r"\b(?:account|acct|iban|swift|routing|sort code|ifsc)\b\s*[:#-]?\s*([A-Z0-9-]{6,})",
    re.IGNORECASE,
)


def sanitize_text(text: str) -> str:
    """Mask emails, phone numbers, and bank identifiers.

    Args:
        text: Raw business document text.

    Returns:
        Sanitized text with sensitive values masked.
    """
    cleaned_text = text.strip()
    if not cleaned_text:
        return ""

    cleaned_text = EMAIL_PATTERN.sub(EMAIL_REPLACEMENT, cleaned_text)
    cleaned_text = PHONE_PATTERN.sub(PHONE_REPLACEMENT, cleaned_text)
    cleaned_text = BANK_HINT_PATTERN.sub(
        lambda match: match.group(0).replace(match.group(1), BANK_REPLACEMENT),
        cleaned_text,
    )
    cleaned_text = re.sub(r"\s+", " ", cleaned_text).strip()
    return cleaned_text
