from __future__ import annotations

import re


def normalize_text(text: str) -> str:
    return " ".join(text.strip().split())


def split_sentences(text: str) -> list[str]:
    cleaned = text.strip()
    if not cleaned:
        return []
    parts = re.split(r"(?<=[.!?])\s+", cleaned)
    return [part.strip() for part in parts if part.strip()]
