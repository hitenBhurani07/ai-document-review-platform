"""Text summarization helpers built on HuggingFace Transformers."""

from __future__ import annotations

import logging
import re
from functools import lru_cache
from typing import List

from utils.text_utils import normalize_text, split_sentences

try:
    from transformers import pipeline
except Exception:  # pragma: no cover - optional dependency
    pipeline = None


logger = logging.getLogger(__name__)

MODEL_NAME = "facebook/bart-large-cnn"


@lru_cache(maxsize=1)
def _get_summarizer():
    if pipeline is None:
        raise RuntimeError("transformers is not available")
    logger.info("Loading summarization model...")
    return pipeline("summarization", model=MODEL_NAME)


def _summarization_supported() -> bool:
    if pipeline is None:
        return False
    try:
        from transformers.pipelines import SUPPORTED_TASKS

        return "summarization" in SUPPORTED_TASKS
    except Exception:
        return False


def _split_text_into_chunks(text: str, max_words: int = 450) -> List[str]:
    words = text.split()
    if not words:
        return []

    chunks: List[str] = []
    for start in range(0, len(words), max_words):
        chunk = " ".join(words[start : start + max_words]).strip()
        if chunk:
            chunks.append(chunk)
    return chunks


def _clean_summary(summary: str) -> str:
    cleaned = " ".join(summary.split()).strip()
    cleaned = re.sub(r"\s+([.,:;])", r"\1", cleaned)
    return cleaned


def _fallback_summary(text: str, max_sentences: int = 3) -> str:
    sentences = split_sentences(text)
    if not sentences:
        return normalize_text(text)
    return _clean_summary(" ".join(sentences[:max_sentences]))


def summarize_text(text: str) -> str:
    """Summarize text with transformers, falling back to the first three sentences."""
    cleaned_text = normalize_text(text)
    if not cleaned_text:
        return ""

    if not _summarization_supported():
        return _fallback_summary(cleaned_text)

    try:
        summarizer = _get_summarizer()
        chunks = _split_text_into_chunks(cleaned_text)
        if not chunks:
            return _fallback_summary(cleaned_text)

        summaries: List[str] = []
        for chunk in chunks:
            result = summarizer(
                chunk,
                max_length=110,
                min_length=25,
                do_sample=False,
            )
            if result and "summary_text" in result[0]:
                summaries.append(_clean_summary(result[0]["summary_text"]))

        final_summary = _clean_summary(" ".join(summaries))
        if not final_summary:
            return _fallback_summary(cleaned_text)

        input_words = cleaned_text.split()
        summary_words = final_summary.split()
        if input_words and len(summary_words) >= int(0.9 * len(input_words)):
            return _fallback_summary(cleaned_text)

        return final_summary
    except Exception as exc:
        logger.warning("Summarizer unavailable, using fallback: %s", exc)
        return _fallback_summary(cleaned_text)
