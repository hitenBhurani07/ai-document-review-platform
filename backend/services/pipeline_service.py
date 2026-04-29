"""End-to-end document analysis pipeline helpers."""

from __future__ import annotations

from typing import Any, Dict

from backend.services.nlp_service import (
    detect_risks,
    extract_entities,
    generate_action_items,
    summarize_document,
)
from utils.privacy import sanitize_text
from utils.text_utils import normalize_text


def _score_confidence(summary: str, entities: Dict[str, list[str]], risk_flags: list[str]) -> str:
    score = 0
    if summary:
        score += 2
    if entities.get("organizations"):
        score += 1
    if entities.get("dates"):
        score += 1
    if entities.get("amounts"):
        score += 1
    if entities.get("invoice_ids"):
        score += 1
    if risk_flags:
        score += 1

    if score >= 5:
        return "High"
    if score >= 3:
        return "Medium"
    return "Low"


def analyze_document(input_text: str) -> Dict[str, Any]:
    """Analyze a business document and return the structured insights."""
    sanitized_text = sanitize_text(input_text)
    cleaned_text = normalize_text(sanitized_text)
    summary = summarize_document(cleaned_text)
    entities = extract_entities(cleaned_text)
    risk_flags = detect_risks(cleaned_text)
    action_items = generate_action_items(cleaned_text, risk_flags, entities)
    confidence_score = _score_confidence(summary, entities, risk_flags)

    return {
        "summary": summary,
        "key_entities": entities,
        "risk_flags": risk_flags,
        "action_items": action_items,
        "confidence_score": confidence_score,
    }
