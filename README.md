# Document Risk Intelligence Platform / AI-Powered Document Review & Risk Insights Platform

Beginner-friendly business document intelligence system for summarizing contracts, invoices, audit notes, vendor agreements, policy updates, and meeting minutes.

## Problem Statement

Manual review of business documents is time-consuming, error-prone, and often delays decision-making in consulting, audit, and finance operations.

## Solution

This platform automates document review by generating concise summaries, extracting key entities, highlighting risk keywords, and recommending next actions in a structured JSON format.

## Features

- Upload .txt documents or paste text
- Smart summarization with a simple fallback
- Entity extraction for organizations, dates, amounts, and invoice IDs
- Risk keyword detection (penalty, overdue, breach, dispute, non-compliance)
- Missing information alerts and recommended action items
- Clean JSON output for dashboards or reporting
- Beginner-friendly FastAPI + JavaScript stack
- Sample documents included in `data/knowledge/` for quick testing

## Tech Stack

- Python
- FastAPI
- spaCy (optional for organization extraction)
- transformers (optional for summarization)
- HTML, CSS, JavaScript

## Installation

1. Create and activate a virtual environment:

```bash
python -m venv .venv
.venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. (Optional) Install the spaCy English model for better organization extraction:

```bash
python -m spacy download en_core_web_sm
```

## Run Backend

```bash
uvicorn backend.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

## Run Frontend

Open `frontend/index.html` in a browser, or serve it with a local static server (e.g., Live Server in VS Code).

## Sample Output

```json
{
  "summary": "Short business summary",
  "key_entities": {
    "organizations": ["ABC Technologies", "Sigma Logistics"],
    "dates": ["1 January 2026"],
    "amounts": ["Rs 4,50,000"],
    "invoice_ids": ["INV-20431"]
  },
  "risk_flags": ["penalty", "overdue"],
  "action_items": [
    "Review penalty clauses and quantify potential exposure.",
    "Follow up on overdue payment and confirm the resolution timeline."
  ],
  "confidence_score": "High"
}
```

## Use Cases

- Contract review and compliance checks
- Invoice monitoring and overdue alerts
- Vendor agreement validation
- Audit meeting notes summarization
- Policy update impact analysis

## Future Scope

- Parse PDF and DOCX files
- Export insights to CSV/Excel
- Add a review workflow and approvals
- Add configurable risk keyword dictionaries

## Resume-Ready Description

AI-Powered Document Review & Risk Insights Platform
Python, FastAPI, NLP, JavaScript, HTML/CSS

- Developed a document intelligence platform to summarize business reports, contracts, and invoices.
- Implemented entity extraction for dates, monetary values, and organization names.
- Added rule-based risk detection for penalties, overdue payments, and compliance concerns.
- Built REST APIs and responsive dashboard UI for streamlined review workflows.
