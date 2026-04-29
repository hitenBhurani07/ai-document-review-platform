# 05 Backend Deep Dive

## What The Backend Does

The backend is the processing brain of the AI-Powered Document Review & Risk Insights Platform. The frontend collects input, but the backend performs the actual document analysis.

The backend is responsible for:

- Running the FastAPI web server.
- Receiving pasted text or uploaded `.txt` files.
- Validating requests.
- Handling errors.
- Calling the NLP pipeline.
- Returning structured JSON responses.

In simple words, the backend accepts a business document, processes it, and returns insights.

## Backend Folder Structure

Important backend files:

| File | Role |
| --- | --- |
| `backend/main.py` | Creates the FastAPI app and configures middleware |
| `backend/api/routes.py` | Defines API endpoints |
| `backend/schemas/document.py` | Defines request and response schemas |
| `backend/services/pipeline_service.py` | Controls the document analysis pipeline |
| `backend/services/nlp_service.py` | Performs NLP logic and rule-based business analysis |
| `utils/privacy.py` | Masks sensitive values |
| `utils/text_utils.py` | Cleans and normalizes text |
| `utils/summarizer.py` | Provides summarization support and fallback logic |

This structure is good because it separates responsibilities.

## FastAPI Basics

FastAPI is a Python framework used to build APIs. An API lets the frontend communicate with backend code.

Example:

```text
Frontend: "Please analyze this document."
Backend: "Here is the summary, entities, risks, and actions."
```

FastAPI is useful because it provides:

- Clean route definitions.
- JSON request and response handling.
- Automatic API documentation at `/docs`.
- Validation with Pydantic.
- Good performance for web APIs.

## `backend/main.py`

This file starts the backend application.

Main responsibilities:

- Create the FastAPI app.
- Add metadata such as title, description, and version.
- Configure CORS.
- Include the API router.
- Define a root endpoint.

### App Creation

The app is created with:

```python
app = FastAPI(
    title="AI-Powered Document Review & Risk Insights Platform",
    description="Analyze business documents...",
    version="1.0.0",
)
```

This metadata appears in FastAPI documentation.

### CORS Middleware

The backend includes CORS middleware so that the browser frontend can call the backend.

Why this matters:

- Frontend may run on `localhost:5500`.
- Backend may run on `localhost:8000`.
- Browsers block cross-origin requests unless CORS allows them.

Interview answer:

> I configured CORS because the frontend and backend can run on different local ports during development. CORS allows the browser frontend to safely call the FastAPI backend.

### Router Inclusion

`main.py` includes routes from `backend/api/routes.py`:

```python
app.include_router(api_router)
```

This keeps `main.py` clean and avoids putting all endpoints in one file.

## Routes

Routes are API endpoints. They define what URL the frontend can call.

The project has three main backend endpoints:

| Endpoint | Method | Purpose |
| --- | --- | --- |
| `/` | GET | Confirms app is running |
| `/health` | GET | Health check |
| `/analyze-text` | POST | Analyze pasted text |
| `/upload-document` | POST | Analyze uploaded `.txt` file |

## GET Requests

GET requests usually retrieve information.

In this project:

```text
GET /
```

returns a message that the platform is running.

```text
GET /health
```

returns:

```json
{ "status": "ok" }
```

Health checks are useful for testing whether the server is alive.

## POST Requests

POST requests send data to the backend for processing.

This project uses POST because the user is sending document text or a file to be analyzed.

### Why POST Instead Of GET?

GET is not ideal for document text because:

- GET parameters are visible in the URL.
- URLs have length limits.
- Document text may be large.
- POST is the standard method for sending request bodies.

Interview answer:

> I used POST for analysis endpoints because the frontend sends document content to the backend. POST supports request bodies and is more appropriate for processing user-submitted data.

## `/analyze-text` Endpoint

This endpoint accepts pasted text as JSON.

Flow:

```text
Frontend sends JSON
        |
        v
Route receives DocumentRequest
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

Example request:

```json
{
  "text": "Invoice INV-20431 for $7,500 is overdue and may trigger penalty."
}
```

Example response:

```json
{
  "summary": "Invoice INV-20431 for $7,500 is overdue and may trigger penalty.",
  "key_entities": {
    "organizations": [],
    "dates": [],
    "amounts": ["$7,500"],
    "invoice_ids": ["INV-20431"]
  },
  "risk_flags": ["penalty", "overdue"],
  "action_items": [
    "Follow up on overdue payment and confirm the resolution timeline.",
    "Review penalty clauses and quantify potential exposure."
  ],
  "confidence_score": "Medium"
}
```

## `/upload-document` Endpoint

This endpoint accepts uploaded `.txt` files.

The backend checks:

- File has a filename.
- File extension is `.txt`.
- File can be decoded.
- File is not empty.

Flow:

```text
Frontend uploads file
        |
        v
Backend checks filename
        |
        v
Backend checks .txt extension
        |
        v
Backend reads bytes
        |
        v
Backend decodes as UTF-8
        |
        v
Backend calls pipeline
        |
        v
Backend returns JSON
```

### Why Only `.txt` Files Currently?

The current project supports `.txt` because plain text is simple and reliable for an internship-level NLP project. PDF, DOCX, and scanned image support can be added later.

Interview answer:

> I started with `.txt` support to focus on the core NLP and API pipeline. In future scope, I would add PDF parsing, DOCX support, and OCR for scanned documents.

## File Upload Handling

FastAPI uses `UploadFile` for file uploads.

The route reads file bytes:

```python
raw_bytes = file.file.read()
text = raw_bytes.decode("utf-8", errors="ignore").strip()
```

This converts the uploaded file into text that the pipeline can analyze.

### What Is Multipart Form Data?

Multipart form data is the format commonly used when uploading files from a browser. JavaScript creates it using `FormData`.

The frontend sends:

```javascript
const formData = new FormData();
formData.append("file", file);
```

## JSON Responses

The backend returns JSON because JavaScript can easily read JSON.

JSON is structured like key-value pairs:

```json
{
  "summary": "...",
  "risk_flags": ["penalty", "breach"]
}
```

The response is validated using `DocumentResponse`.

## Schema Validation

Schemas are defined in `backend/schemas/document.py`.

### `DocumentRequest`

This schema validates input for pasted text:

```python
class DocumentRequest(BaseModel):
    text: str = Field(..., min_length=1)
```

It means text is required and must contain at least one character.

### `DocumentResponse`

This schema defines output:

- `summary`
- `key_entities`
- `risk_flags`
- `action_items`
- `confidence_score`

### Why Validation Matters

Validation helps prevent unpredictable API behavior.

Benefits:

- Frontend receives consistent data.
- API documentation is accurate.
- Invalid requests are caught early.
- Code becomes easier to maintain.

## Pipeline Service

`backend/services/pipeline_service.py` controls the analysis workflow.

It performs:

1. Privacy sanitization.
2. Text normalization.
3. Summarization.
4. Entity extraction.
5. Risk detection.
6. Action item generation.
7. Confidence scoring.

The route does not need to know these details. It simply calls:

```python
result = analyze_document(text)
```

This is a clean design.

## NLP Service

`backend/services/nlp_service.py` contains:

- `summarize_document`
- `extract_entities`
- `detect_risks`
- `generate_action_items`

### Why This Logic Is Separate

Keeping NLP in a service file makes future upgrades easier. For example:

- Replace keyword matching with ML classification.
- Add better NER.
- Add LLM-based summaries.
- Improve action recommendations.

Routes do not need to change much if service internals improve.

## Error Handling

The backend uses `HTTPException` for user-facing errors.

Examples:

| Situation | Status Code | Message |
| --- | --- | --- |
| Empty text | 400 | Text input cannot be empty |
| Missing filename | 400 | No filename provided |
| Wrong file type | 400 | Only .txt files are supported |
| Empty uploaded file | 400 | Uploaded file is empty |
| Unexpected processing error | 500 | Error analyzing text/upload |

### 400 vs 500

- **400 Bad Request:** User sent invalid input.
- **500 Internal Server Error:** Something unexpected failed inside the server.

Interview answer:

> I used 400 errors for invalid user inputs like empty text or unsupported file type, and 500 errors for unexpected backend processing failures.

## Logging

The route file uses Python logging to record analysis events and errors.

Logging is useful because:

- It helps debug issues.
- It records backend activity.
- It helps identify failures during testing.

In production, logs can be sent to cloud monitoring tools.

## Scalability Basics

The current backend is suitable for local demos and small-scale use. To scale it for real business usage, we could add:

- Multiple Uvicorn workers.
- Background task queues for large documents.
- Caching for repeated inputs.
- Database storage for reports.
- Authentication and role-based access.
- File size limits.
- Cloud deployment.
- Separate model inference service.

### Why Long Documents Need Special Handling

Large documents can take longer to summarize. For production, heavy NLP tasks should not block the API for too long. A better design could:

1. Upload document.
2. Create a job ID.
3. Process in background.
4. Let user check status.
5. Show report when ready.

## Security Basics

Important backend security improvements:

- Validate file type and size.
- Sanitize uploaded content.
- Avoid storing sensitive data unnecessarily.
- Add authentication for users.
- Use HTTPS in production.
- Add rate limiting.
- Log errors without exposing sensitive document content.

## Beginner-Friendly Backend Explanation

Think of the backend as an office assistant:

1. It receives the document.
2. It checks whether the document is valid.
3. It cleans the document.
4. It reads the document using NLP rules.
5. It writes a structured report.
6. It sends the report back to the dashboard.

## Strong Interview Answer

> The backend is built with FastAPI. `main.py` creates the app, configures CORS, and includes routes. `routes.py` defines endpoints for health check, pasted text analysis, and file upload analysis. Pydantic schemas validate the input and output. The route layer calls `analyze_document` in the pipeline service, which sanitizes and normalizes text, summarizes it, extracts entities, detects risk keywords, generates action items, and calculates a confidence score. The final result is returned as JSON to the frontend.

## Interview Tip

When explaining backend code, separate route responsibility from business logic. Say: "Routes handle HTTP, services handle processing."

## Common Mistakes

- Saying FastAPI directly performs NLP. FastAPI only exposes the API.
- Forgetting to mention validation with Pydantic.
- Not knowing why POST is used.
- Ignoring file validation.
- Calling all errors server errors. Invalid input should be a 400-level error.

## 5 Rapid Fire Questions

1. What does `main.py` do?
2. What is the purpose of `routes.py`?
3. Why is POST used for document analysis?
4. What does Pydantic validate?
5. What happens if a user uploads a non-`.txt` file?

## 30 Second Revision Summary

The backend uses FastAPI to expose APIs for pasted text and `.txt` file upload. Routes validate input, handle errors, and call the pipeline service. Pydantic schemas define request and response structure. The pipeline sanitizes, cleans, summarizes, extracts entities, detects risks, generates actions, calculates confidence, and returns JSON to the frontend. The backend is modular, explainable, and easy to extend.
