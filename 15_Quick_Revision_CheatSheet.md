# 15 Quick Revision CheatSheet

## One-Night-Before Summary

Project name: **AI-Powered Document Review & Risk Insights Platform**

One-line explanation:

> It converts business documents into summaries, extracted entities, risk alerts, action items, and confidence scores using a FastAPI backend and JavaScript dashboard.

Main problem solved:

- Manual document review is slow.
- Important risks are easy to miss.
- Review quality varies by person.
- Business teams need faster structured insights.

Main users:

- Consulting teams
- Audit teams
- Finance teams
- Compliance teams
- Operations teams
- Procurement teams

## Core Features

- Paste text input.
- `.txt` file upload.
- Document summarization.
- Organization/date/amount/invoice ID extraction.
- Risk keyword detection.
- Recommended action item generation.
- Confidence score.
- Dashboard cards.
- JSON API response.

## Best 30 Second Project Answer

> I built an AI-Powered Document Review and Risk Insights Platform for business teams. Users can paste text or upload a `.txt` document such as a contract, invoice, audit note, or compliance memo. The FastAPI backend runs an NLP pipeline to sanitize and clean the text, summarize it, extract key entities like organizations, dates, amounts, and invoice IDs, detect risk keywords like penalty, overdue, breach, liability, fraud, and dispute, and generate action items. The JavaScript frontend displays the structured JSON result in dashboard cards. The project saves review time and improves consistency for consulting, audit, finance, and compliance workflows.

## Architecture Cheat Sheet

```text
Frontend
  index.html
  styles.css
  app.js
      |
      v
API request using fetch
      |
      v
FastAPI backend
  main.py
  routes.py
      |
      v
Schemas
  document.py
      |
      v
Pipeline service
  pipeline_service.py
      |
      v
NLP service and utils
  nlp_service.py
  text_utils.py
  privacy.py
  summarizer.py
      |
      v
JSON response
      |
      v
Dashboard result cards
```

## Pipeline Cheat Sheet

```text
Input text
    |
    v
Sanitize private data
    |
    v
Normalize whitespace
    |
    v
Summarize document
    |
    v
Extract entities
    |
    v
Detect risk keywords
    |
    v
Generate action items
    |
    v
Score confidence
    |
    v
Return JSON
```

## Tech Stack Cheat Sheet

| Technology | Why Used |
| --- | --- |
| Python | NLP and backend logic |
| FastAPI | Modern API framework |
| Pydantic | Request/response validation |
| HTML | Page structure |
| CSS | Dashboard styling |
| JavaScript | User interaction and API calls |
| Fetch API | Connect frontend to backend |
| Regex | Extract dates, amounts, invoice IDs, risk terms |
| spaCy | Optional organization extraction |
| Transformers | Optional summarization |
| Git/GitHub | Version control and portfolio |

## Backend Quick Points

- `main.py` creates the app and configures CORS.
- `routes.py` defines endpoints.
- `/health` checks server status.
- `/analyze-text` handles pasted text.
- `/upload-document` handles `.txt` files.
- Pydantic validates input and output.
- Pipeline service controls analysis steps.
- NLP service performs summarization, extraction, risk detection, and action generation.

## Frontend Quick Points

- `index.html` contains UI structure.
- `styles.css` creates business dashboard design.
- `app.js` handles tabs, input, fetch requests, loading, errors, and result rendering.
- Results are shown as cards.
- Entities are shown as chips.
- Risks and actions are shown as lists.
- Confidence is shown as a badge.

## API Quick Points

Main endpoints:

| Endpoint | Method | Purpose |
| --- | --- | --- |
| `/` | GET | Root status |
| `/health` | GET | Health check |
| `/analyze-text` | POST | Analyze pasted text |
| `/upload-document` | POST | Analyze `.txt` file |

Main response fields:

- `summary`
- `key_entities`
- `risk_flags`
- `action_items`
- `confidence_score`

## NLP Quick Points

NLP means Natural Language Processing.

Used for:

- Text cleaning
- Summarization
- Entity extraction
- Risk keyword detection
- Action generation

Key entities:

- Organizations
- Dates
- Amounts
- Invoice IDs

## Risk Keywords

Important risk terms:

- penalty
- overdue
- delay
- breach
- terminated
- termination
- liability
- escalation
- urgent
- fraud
- dispute
- non-compliance

Risk logic:

```text
Convert text to lowercase
Check predefined keywords
Remove duplicates
Return risk flags
Generate actions
```

## Strong Answers To Memorize

### Why FastAPI?

FastAPI is modern, fast, and built for APIs. It provides automatic documentation, Pydantic validation, clean route definitions, and good performance. It is a better fit than Flask for a structured JSON API project.

### Why Python?

Python is excellent for NLP and backend development. It has strong libraries for text processing, regex, spaCy, transformers, FastAPI, and testing. It also keeps the code readable.

### Why regex?

Regex is useful for extracting predictable business patterns such as dates, amounts, invoice IDs, phone numbers, and emails. It is fast, explainable, and practical.

### Why POST?

POST is used because document text and files are sent to the backend for processing. GET is not suitable for long or sensitive document content.

### Why JSON?

JSON is structured, lightweight, easy for FastAPI to return, and easy for JavaScript to parse and display.

### Why this project is useful for KPMG?

KPMG and similar consulting firms handle audits, risk reviews, compliance projects, and client documents. This project speeds up first-pass review, highlights risk language, and produces structured insights for analysts.

## Limitations To Admit

- Current version supports `.txt`, not PDF or scanned documents.
- Keyword detection may not understand context deeply.
- It may produce false positives.
- It may miss synonyms not in the keyword list.
- Confidence score is heuristic, not ML probability.
- It assists human reviewers, not replaces them.

## Future Improvements

- PDF parsing
- OCR
- DOCX support
- User login
- Database storage
- Saved report history
- Dashboard analytics
- Risk severity scoring
- LLM-based summarization
- Multilingual support
- Role-based access
- Cloud deployment
- Export reports

## Top 20 Questions

### 1. Explain your project.

It is a document intelligence platform that analyzes business text and returns summary, entities, risks, actions, and confidence score.

### 2. Why did you build it?

To reduce manual document review time and improve consistency in identifying important business details and risk terms.

### 3. What problem does it solve?

It solves the problem of slow, inconsistent, and error-prone manual review of business documents.

### 4. What is the tech stack?

Python, FastAPI, Pydantic, HTML, CSS, JavaScript, regex, optional spaCy, optional transformers, Git, and GitHub.

### 5. Why FastAPI?

Because it is modern, API-focused, supports validation, and provides automatic docs.

### 6. Why Python?

Because Python has strong NLP and backend development support.

### 7. How does the frontend communicate with backend?

Using JavaScript `fetch` requests to FastAPI endpoints.

### 8. What endpoints are used?

`/health`, `/analyze-text`, and `/upload-document`.

### 9. What is the pipeline?

Sanitize, normalize, summarize, extract entities, detect risks, generate actions, score confidence, return JSON.

### 10. What entities are extracted?

Organizations, dates, amounts, and invoice IDs.

### 11. How are risks detected?

By scanning lowercase text for predefined business risk keywords.

### 12. What are action items?

Recommended next steps generated from detected risks and missing details.

### 13. What is the confidence score?

A rule-based indicator showing whether the analysis found enough useful information.

### 14. What are project limitations?

Limited file support, rule-based risk logic, weak context understanding, and no database in the current version.

### 15. How would you improve it?

Add PDF/OCR, database, login, analytics, LLM summaries, risk severity, and cloud deployment.

### 16. How is it useful for finance?

It detects overdue invoices, amounts, invoice IDs, penalties, and follow-up actions.

### 17. How is it useful for audit?

It summarizes audit notes, flags compliance risks, and generates remediation actions.

### 18. How is it useful for consulting?

It helps analysts review client documents faster and prepare structured findings.

### 19. Why is modular architecture used?

It separates frontend, routes, schemas, services, and utilities, making the project easier to maintain and extend.

### 20. What is your strongest project point?

The complete end-to-end flow: user input to API to NLP pipeline to JSON response to dashboard visualization.

## Final Memory Hooks

Remember these five words:

```text
Summarize
Extract
Detect
Recommend
Display
```

Remember this business value line:

```text
The project reduces first-pass review time and improves risk visibility.
```

Remember this limitation line:

```text
It is an assistive first-pass review tool, not a replacement for expert judgment.
```

## Interview Tip

In the final interview, do not sound like you memorized definitions. Speak like you built it: "I designed it this way because..."

## Common Mistakes

- Forgetting the business problem.
- Overclaiming the AI capability.
- Not knowing the request flow.
- Confusing frontend and backend responsibilities.
- Forgetting future improvements.

## 5 Rapid Fire Questions

1. What are the five output fields?
2. What does `POST /analyze-text` do?
3. What file controls the pipeline?
4. Name three risk keywords.
5. What is the biggest limitation?

## 30 Second Revision Summary

This is a full-stack business document intelligence project. The user submits text or a `.txt` file through a JavaScript dashboard. FastAPI receives the request, validates it, runs a Python NLP pipeline, and returns JSON with summary, entities, risk flags, action items, and confidence score. It helps consulting, audit, finance, and compliance teams review documents faster and more consistently. Future scope includes PDF/OCR, database, login, analytics, LLM summaries, and deployment.
