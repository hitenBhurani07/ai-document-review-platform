from __future__ import annotations

from backend.services.pipeline_service import analyze_document


def test_summary_not_empty() -> None:
    text = (
        "ABC Technologies signed a 12 month agreement with Sigma Logistics effective 1 January 2026. "
        "Payment of Rs 4,50,000 is due within 30 days."
    )

    result = analyze_document(text)

    assert result["summary"]


def test_risk_flags_list_exists() -> None:
    text = "The invoice is overdue and a penalty may apply if payment is delayed."

    result = analyze_document(text)

    assert isinstance(result["risk_flags"], list)


def test_dates_extraction_works() -> None:
    text = "The contract starts on 1 January 2026 and ends on 12/31/2026."

    result = analyze_document(text)

    assert result["key_entities"]["dates"]


def test_amount_extraction_works() -> None:
    text = "Total amount due is USD 12,500 with a late fee if unpaid."

    result = analyze_document(text)

    assert result["key_entities"]["amounts"]
