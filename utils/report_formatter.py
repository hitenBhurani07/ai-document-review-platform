from __future__ import annotations

from typing import Dict, List


def _join(items: List[str]) -> str:
    return ", ".join(items) if items else "None detected."


def generate_report_sections(
    summary: str,
    entities: Dict[str, List[str]],
    risk_flags: List[str],
    action_items: List[str],
) -> Dict[str, str]:
    """Build a simple business report with human-readable sections."""
    summary_text = summary or "Summary not available."

    important_entities = [
        f"Organizations: {_join(entities.get('organizations', []))}",
        f"Dates: {_join(entities.get('dates', []))}",
        f"Amounts: {_join(entities.get('amounts', []))}",
        f"Invoice IDs: {_join(entities.get('invoice_ids', []))}",
    ]

    return {
        "Executive Summary": summary_text,
        "Key Risks": _join(risk_flags),
        "Important Entities": " | ".join(important_entities),
        "Recommended Actions": _join(action_items),
    }
