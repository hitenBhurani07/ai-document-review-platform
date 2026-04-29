# 03 Project Architecture

## Architecture Meaning

Architecture means the way a software system is organized. It explains:

- Which parts exist.
- What each part is responsible for.
- How data moves from one part to another.
- Why the project is divided into modules.

For this project, the architecture is a simple full-stack web application:

```text
Frontend dashboard
        |
        v
API request
        |
        v
FastAPI backend routes
        |
        v
Pipeline service
        |
        v
NLP service and utility helpers
        |
        v
Structured JSON response
        |
        v
Frontend result cards
```

The architecture is intentionally modular. Each file has a clear job. This makes the project easier to understand, test, debug, and explain during interviews.

## High-Level Architecture Diagram

```text
User
 |
 | pastes text or uploads .txt file
 v
frontend/index.html
frontend/app.js
 |
 | fetch POST request
 v
backend/main.py
 |
 | includes API router
 v
backend/api/routes.py
 |
 | validates input and calls pipeline
 v
backend/services/pipeline_service.py
 |
 | orchestrates cleaning, NLP, risk logic
 v
backend/services/nlp_service.py
utils/text_utils.py
utils/privacy.py
utils/summarizer.py
 |
 | returns Python dictionary
 v
Pydantic response schema
 |
 | JSON response
 v
frontend result cards
```

## Main Layers

## 1. Frontend Layer

The frontend is the part the user sees. It is inside the `frontend` folder.

Important files:

| File | Purpose |
| --- | --- |
| `frontend/index.html` | Defines the webpage structure |
| `frontend/styles.css` | Styles the dashboard |
| `frontend/app.js` | Handles user actions and API calls |

### What The Frontend Does

The frontend allows the user to:

- Paste document text.
- Upload a `.txt` file.
- Insert sample text.
- Click "Analyze Document."
- View summary, entities, risks, action items, and confidence score.

### Why The Frontend Is Separate

The frontend should not contain heavy NLP logic. Its job is presentation and interaction. The backend handles processing.

This separation makes the system cleaner:

- Frontend focuses on user experience.
- Backend focuses on analysis.
- API connects both.

## 2. API Request Layer

The frontend communicates with the backend using HTTP requests.

There are two main request types:

| User Action | Endpoint | Request Type |
| --- | --- | --- |
| Paste text and analyze | `POST /analyze-text` | JSON body |
| Upload file and analyze | `POST /upload-document` | Multipart form data |

### Why API Requests Matter

The API layer allows the frontend and backend to work independently. The frontend does not need to know how summarization or risk detection works. It only needs to send input and receive output.

Example:

```text
Frontend sends:
{ "text": "Vendor agreement..." }

Backend returns:
{
  "summary": "...",
  "key_entities": {...},
  "risk_flags": [...],
  "action_items": [...],
  "confidence_score": "High"
}
```

## 3. FastAPI Application Layer

The backend starts in `backend/main.py`.

Responsibilities:

- Create the FastAPI app.
- Set project title, description, and version.
- Configure CORS.
- Include API routes.
- Provide a root endpoint.

### CORS In The Architecture

CORS stands for Cross-Origin Resource Sharing.

In this project, the frontend may run from:

- `http://127.0.0.1:5500`
- `http://localhost:5500`

The backend may run from:

- `http://127.0.0.1:8000`

Because these are different origins, CORS settings allow the browser frontend to call the backend safely during development.

### Root Endpoint

The root endpoint `/` returns a simple message showing that the backend is running.

This is useful for:

- Quick testing.
- Deployment checks.
- Interview demo verification.

## 4. Routes Layer

Routes are defined in `backend/api/routes.py`.

The route layer is responsible for:

- Defining API endpoints.
- Receiving input.
- Performing basic validation.
- Calling the pipeline service.
- Returning the response.
- Handling errors.

### Important Routes

| Route | Method | Purpose |
| --- | --- | --- |
| `/health` | GET | Checks if API is alive |
| `/analyze-text` | POST | Analyzes pasted text |
| `/upload-document` | POST | Analyzes uploaded `.txt` file |

### Analyze Text Flow

```text
POST /analyze-text
        |
        v
Receive JSON body
        |
        v
Check text is not empty
        |
        v
Call analyze_document(text)
        |
        v
Return DocumentResponse
```

### Upload Document Flow

```text
POST /upload-document
        |
        v
Receive uploaded file
        |
        v
Check filename exists
        |
        v
Allow only .txt files
        |
        v
Decode file content as UTF-8
        |
        v
Check content is not empty
        |
        v
Call analyze_document(text)
        |
        v
Return DocumentResponse
```

## 5. Schema Layer

Schemas are defined in `backend/schemas/document.py`.

Schemas describe the shape of data.

### Request Schema

`DocumentRequest` expects:

```text
text: string
```

This is used by `POST /analyze-text`.

### Response Schema

`DocumentResponse` returns:

- `summary`
- `key_entities`
- `risk_flags`
- `action_items`
- `confidence_score`

### Entity Schema

`EntityBlock` contains:

- `organizations`
- `dates`
- `amounts`
- `invoice_ids`

### Why Schemas Matter

Schemas help enforce consistency. The frontend can rely on the backend response having the same structure every time.

Without schemas, one response might use `risk_flags`, another might use `risks`, and the frontend could break.

## 6. Pipeline Service Layer

The pipeline service is in `backend/services/pipeline_service.py`.

This is the orchestration layer. It does not do every NLP task itself. Instead, it calls the correct helper functions in the correct order.

Pipeline order:

```text
sanitize_text(input_text)
        |
        v
normalize_text(sanitized_text)
        |
        v
summarize_document(cleaned_text)
        |
        v
extract_entities(cleaned_text)
        |
        v
detect_risks(cleaned_text)
        |
        v
generate_action_items(cleaned_text, risks, entities)
        |
        v
_score_confidence(summary, entities, risks)
        |
        v
return structured dictionary
```

### Why The Pipeline Layer Is Useful

The pipeline layer acts like a manager. It coordinates the steps and keeps route files clean.

Routes should not contain long NLP logic. If all logic were inside `routes.py`, the file would become hard to maintain. The pipeline separates web handling from document intelligence logic.

## 7. NLP Service Layer

The NLP service is in `backend/services/nlp_service.py`.

It contains the main document analysis functions:

- `summarize_document`
- `extract_entities`
- `detect_risks`
- `generate_action_items`

### Responsibilities

This layer performs business text analysis:

- Uses summarization to shorten long text.
- Uses regex and optional spaCy to identify entities.
- Uses keyword matching to detect risks.
- Uses rule-based mapping to produce actions.

### Why NLP Logic Is In A Separate File

This makes the code easier to extend. If you later replace rule-based risk detection with a machine learning model, you can update `nlp_service.py` without rewriting API routes or frontend code.

## 8. Utility Layer

Utility files contain reusable helper functions.

| File | Purpose |
| --- | --- |
| `utils/text_utils.py` | Normalizes whitespace and splits sentences |
| `utils/privacy.py` | Masks emails, phone numbers, and bank identifiers |
| `utils/summarizer.py` | Handles transformer or fallback summarization |
| `utils/report_formatter.py` | Formats report sections |
| `utils/rag_retriever.py` | Provides local retrieval support for future grounding |

### Why Utilities Matter

Utilities prevent repeated code. For example, if text normalization is needed in multiple places, it should live in one helper function instead of being copied everywhere.

## 9. JSON Response Layer

The backend returns a JSON response.

JSON is easy for JavaScript to read and display.

Example:

```json
{
  "summary": "Vendor agreement includes payment terms, penalty language, and termination risk.",
  "key_entities": {
    "organizations": ["Blue Harbour Consulting", "Rivergate Foods"],
    "dates": ["1 April 2026", "31 March 2027"],
    "amounts": ["$7,500"],
    "invoice_ids": ["INV-20431"]
  },
  "risk_flags": ["penalty", "breach", "termination", "liability", "escalation"],
  "action_items": [
    "Review penalty clauses and quantify potential exposure.",
    "Validate termination terms and confirm notice requirements."
  ],
  "confidence_score": "High"
}
```

## 10. Frontend Display Layer

Once the frontend receives JSON, `app.js` updates the page.

It places:

- Summary text inside the summary card.
- Entities inside chip lists.
- Risk flags inside a list.
- Action items inside a list.
- Confidence score inside a badge.

This turns raw JSON into a business-friendly dashboard.

## Separation Of Concerns

Separation of concerns means each part of the system has one clear responsibility.

| Concern | File/Layer |
| --- | --- |
| Page structure | `index.html` |
| Styling | `styles.css` |
| Browser logic | `app.js` |
| App creation | `main.py` |
| API endpoints | `routes.py` |
| Data validation | `schemas/document.py` |
| Pipeline orchestration | `pipeline_service.py` |
| NLP logic | `nlp_service.py` |
| Reusable helpers | `utils/` |

### Why It Matters

Separation of concerns improves:

- Readability
- Debugging
- Testing
- Team collaboration
- Future extension

For example, if the UI needs a redesign, we can update frontend files without changing risk detection logic. If the NLP model changes, we can update the backend service without redesigning the UI.

## Modular Architecture

The project uses modular architecture because it is divided into focused modules.

Benefits:

- Easier to explain in interviews.
- Easier to test each function.
- Easier to add features.
- Easier to debug.
- Cleaner than writing all code in one file.

### Interview Example

If asked why you did not write everything in one file, say:

> I separated the project into frontend, routes, schemas, services, and utilities so that each part has a clear responsibility. This makes the code easier to maintain and extend. For example, routes only handle HTTP requests, while the pipeline service handles document processing.

## Complete Request Flow Example

Example user input:

```text
Invoice INV-20431 for $7,500 is overdue. Late payment may trigger penalty and escalation.
```

Flow:

1. User enters text in the textarea.
2. JavaScript reads the text.
3. JavaScript sends `POST /analyze-text`.
4. FastAPI receives the request.
5. Pydantic validates the request body.
6. Route checks that text is not empty.
7. Route calls `analyze_document`.
8. Pipeline sanitizes and normalizes text.
9. NLP service summarizes the text.
10. Entity extractor finds `$7,500` and `INV-20431`.
11. Risk detector finds `overdue`, `penalty`, and `escalation`.
12. Action generator creates follow-up recommendations.
13. Confidence score is calculated.
14. Backend returns JSON.
15. Frontend renders cards.

## Strong Interview Answer

> The architecture has a frontend, API layer, backend route layer, pipeline service, NLP service, utility helpers, and JSON response layer. The frontend collects pasted text or uploaded files and sends them to FastAPI. Routes validate the input and call the pipeline service. The pipeline sanitizes and normalizes the text, then calls NLP functions for summarization, entity extraction, risk detection, and action generation. The result is returned as a Pydantic-validated JSON response and rendered on the dashboard as cards.

## Interview Tip

Use the flow diagram in your explanation. Interviewers like architecture answers that clearly show how data moves through the system.

## Common Mistakes

- Saying the frontend directly performs NLP. In this project, NLP is handled by the backend.
- Forgetting to mention schemas and validation.
- Mixing route logic and pipeline logic in the explanation.
- Saying JSON is displayed directly to the user. The frontend converts JSON into readable cards.
- Ignoring CORS when explaining frontend-backend communication.

## 5 Rapid Fire Questions

1. What file creates the FastAPI app?
2. What file defines API routes?
3. What file orchestrates the analysis pipeline?
4. What does the frontend receive from the backend?
5. Why is modular architecture useful?

## 30 Second Revision Summary

The architecture is frontend to API to backend routes to pipeline service to NLP service to JSON response to UI cards. `index.html`, `styles.css`, and `app.js` manage the user interface. `main.py` creates the FastAPI app, `routes.py` defines endpoints, schemas validate data, `pipeline_service.py` controls the workflow, and `nlp_service.py` performs summarization, extraction, risk detection, and action generation.
