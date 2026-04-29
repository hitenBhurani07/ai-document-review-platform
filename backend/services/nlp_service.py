"""Business document NLP helpers used by the FastAPI routes."""

from __future__ import annotations

import re
from functools import lru_cache
from typing import Dict, Iterable, List

from utils.summarizer import summarize_text
from utils.text_utils import normalize_text

try:
    import spacy
except Exception:  # pragma: no cover - optional dependency
    spacy = None


RISK_KEYWORDS = [
    "penalty",
    "overdue",
    "delay",
    "breach",
    "terminated",
    "termination",
    "liability",
    "escalation",
    "urgent",
    "fraud",
    "dispute",
    "non-compliance",
    "non compliance",
    "noncompliance",
]

DATE_PATTERNS = [
    re.compile(r"\b\d{1,2}[/-]\d{1,2}[/-]\d{2,4}\b"),
    re.compile(r"\b\d{4}-\d{2}-\d{2}\b"),
    re.compile(
        r"\b(?:jan|january|feb|february|mar|march|apr|april|may|jun|june|jul|july|aug|august|"
        r"sep|september|oct|october|nov|november|dec|december)\s+\d{1,2},?\s+\d{4}\b",
        re.IGNORECASE,
    ),
    re.compile(
        r"\b\d{1,2}\s+(?:jan|january|feb|february|mar|march|apr|april|may|jun|june|jul|july|"
        r"aug|august|sep|september|oct|october|nov|november|dec|december)\s+\d{4}\b",
        re.IGNORECASE,
    ),
    re.compile(r"\bQ[1-4]\s+\d{4}\b", re.IGNORECASE),
]

AMOUNT_PATTERN = re.compile(
    r"\b(?:USD|INR|EUR|GBP|Rs\.?)[\s]*\d{1,3}(?:,\d{2,3})*(?:\.\d{1,2})?\b"
    r"|\$\s*\d{1,3}(?:,\d{3})*(?:\.\d{1,2})?",
    re.IGNORECASE,
)

INVOICE_PATTERN = re.compile(r"\b(?:INV|INVOICE)[-\s]?\d{3,}(?:-\d{2,})?\b", re.IGNORECASE)

ORG_PATTERN = re.compile(
    r"\b[A-Z][A-Za-z&]+(?:\s+(?:[A-Z][A-Za-z&]+|&|of|and|the|LLC|Ltd|Inc|Corp|Corporation|Group|Holdings))+\b"
)

ORG_STOPWORDS = {
    "Executive Summary",
    "Key Risks",
    "Important Entities",
    "Recommended Actions",
}


def _dedupe(items: Iterable[str]) -> List[str]:
    seen: set[str] = set()
    ordered: List[str] = []
    for item in items:
        key = item.strip()
        if not key or key in seen:
            continue
        seen.add(key)
        ordered.append(key)
    return ordered


@lru_cache(maxsize=1)
def _load_nlp():
    if spacy is None:
        return None
    try:
        return spacy.load("en_core_web_sm")
    except Exception:
        nlp = spacy.blank("en")
        if "sentencizer" not in nlp.pipe_names:
            nlp.add_pipe("sentencizer")
        return nlp


def summarize_document(text: str) -> str:
    """Summarize business document text."""
    cleaned = normalize_text(text)
    if not cleaned:
        return ""
    return summarize_text(cleaned)


def _collect_pattern_matches(text: str, patterns: Iterable[re.Pattern[str]]) -> List[str]:
    matches: List[str] = []
    for pattern in patterns:
        for match in pattern.finditer(text):
            matches.append(match.group(0).strip())
    return _dedupe(matches)


def extract_entities(text: str) -> Dict[str, List[str]]:
    """Extract organization names, dates, amounts, and invoice IDs."""
    cleaned = normalize_text(text)
    if not cleaned:
        return {
            "organizations": [],
            "dates": [],
            "amounts": [],
            "invoice_ids": [],
        }

    organizations: List[str] = []
    nlp = _load_nlp()
    if nlp is not None:
        doc = nlp(cleaned)
        orgs = [ent.text.strip() for ent in doc.ents if ent.label_ == "ORG"]
        organizations.extend(orgs)

    organizations.extend([match.group(0).strip() for match in ORG_PATTERN.finditer(cleaned)])
    organizations = [org for org in _dedupe(organizations) if org not in ORG_STOPWORDS]

    dates = _collect_pattern_matches(cleaned, DATE_PATTERNS)
    amounts = _dedupe([match.group(0).strip() for match in AMOUNT_PATTERN.finditer(cleaned)])
    invoice_ids = _dedupe([match.group(0).strip() for match in INVOICE_PATTERN.finditer(cleaned)])

    return {
        "organizations": organizations,
        "dates": dates,
        "amounts": amounts,
        "invoice_ids": invoice_ids,
    }


def detect_risks(text: str) -> List[str]:
    """Detect business risk keywords in the document text."""
    lowered = text.lower()
    hits = [keyword for keyword in RISK_KEYWORDS if keyword in lowered]
    return _dedupe(hits)


def generate_action_items(
    text: str,
    risk_flags: List[str],
    entities: Dict[str, List[str]],
) -> List[str]:
    """Create recommended action items based on risks and missing details."""
    actions: List[str] = []
    risk_set = set(risk_flags)

    if "overdue" in risk_set:
        actions.append("Follow up on overdue payment and confirm the resolution timeline.")
    if "penalty" in risk_set:
        actions.append("Review penalty clauses and quantify potential exposure.")
    if "breach" in risk_set:
        actions.append("Escalate the breach to compliance and document next steps.")
    if "delay" in risk_set:
        actions.append("Confirm delivery timelines and update stakeholders on delays.")
    if "terminated" in risk_set or "termination" in risk_set:
        actions.append("Validate termination terms and confirm notice requirements.")
    if "liability" in risk_set:
        actions.append("Review liability caps and confirm mitigation steps.")
    if "dispute" in risk_set:
        actions.append("Capture dispute details and initiate the resolution workflow.")
    if "fraud" in risk_set:
        actions.append("Initiate fraud review and preserve supporting evidence.")
    if "non-compliance" in risk_set or "non compliance" in risk_set or "noncompliance" in risk_set:
        actions.append("Assess compliance gaps and document remediation steps.")
    if "urgent" in risk_set or "escalation" in risk_set:
        actions.append("Assign an owner and set an expedited review deadline.")

    if not entities.get("dates"):
        actions.append("Verify key deadlines and effective dates.")
    if not entities.get("amounts"):
        actions.append("Confirm payment values and billing terms.")
    if not entities.get("invoice_ids") and "invoice" in text.lower():
        actions.append("Confirm the invoice reference number for tracking.")

    return _dedupe(actions)
