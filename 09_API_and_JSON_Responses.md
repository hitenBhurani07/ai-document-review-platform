# 09 API And JSON Responses

## What Is An API?

API stands for Application Programming Interface. It is a way for two software components to communicate.

In this project:

- The frontend is the browser dashboard.
- The backend is the FastAPI application.
- The API is the communication bridge between them.

Simple explanation:

```text
Frontend asks: "Analyze this document."
Backend replies: "Here are the insights."
```

The frontend does not directly run Python NLP code. It sends a request to the backend API.

## Why APIs Matter

APIs matter because they separate the user interface from the processing logic.

Benefits:

- Frontend and backend can be developed separately.
- The same backend can serve different clients.
- The output format stays consistent.
- API endpoints can be tested independently.
- Future mobile or dashboard apps can reuse the backend.

For this project, the API makes the system look like a real business application rather than a simple script.

## What Is REST API?

REST stands for Representational State Transfer. A REST API uses HTTP methods and URLs to perform actions on resources.

Common HTTP methods:

| Method | Common Purpose |
| --- | --- |
| GET | Retrieve data |
| POST | Send data or create/process something |
| PUT | Replace existing data |
| PATCH | Partially update data |
| DELETE | Delete data |

This project mainly uses GET and POST.

## GET vs POST

### GET

GET is used to retrieve information.

Example in this project:

```text
GET /health
```

Response:

```json
{
  "status": "ok"
}
```

GET should not be used to send long document text because GET data usually appears in the URL.

### POST

POST is used to send data to the backend.

Example:

```text
POST /analyze-text
```

The request body contains document text.

Why POST is better here:

- Supports request body.
- Handles larger data.
- Keeps document text out of the URL.
- Matches the idea of processing submitted content.

## API Endpoints In This Project

| Endpoint | Method | Purpose |
| --- | --- | --- |
| `/` | GET | Confirms backend is running |
| `/health` | GET | Returns simple health status |
| `/analyze-text` | POST | Analyzes pasted business text |
| `/upload-document` | POST | Analyzes uploaded `.txt` document |

## Root Endpoint

The root endpoint is:

```text
GET /
```

It returns:

```json
{
  "message": "AI-Powered Document Review & Risk Insights Platform is running.",
  "docs": "/docs"
}
```

This is useful for quickly checking whether the backend started successfully.

## Health Endpoint

The health endpoint is:

```text
GET /health
```

It returns:

```json
{
  "status": "ok"
}
```

Health endpoints are useful in real deployments because monitoring systems can check whether the service is alive.

## Analyze Text Endpoint

Endpoint:

```text
POST /analyze-text
```

Purpose:

- Accept pasted business document text.
- Run the NLP pipeline.
- Return structured insights.

### Example Request

```json
{
  "text": "Vendor agreement between Blue Harbour Consulting and Rivergate Foods. Invoice INV-20431 for $7,500 is overdue and may trigger penalty."
}
```

### Example Response

```json
{
  "summary": "Vendor agreement between Blue Harbour Consulting and Rivergate Foods. Invoice INV-20431 for $7,500 is overdue and may trigger penalty.",
  "key_entities": {
    "organizations": ["Blue Harbour Consulting", "Rivergate Foods"],
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

## Upload Document Endpoint

Endpoint:

```text
POST /upload-document
```

Purpose:

- Accept a `.txt` file.
- Decode file content.
- Run the same document analysis pipeline.
- Return the same response structure.

### Request Type

This endpoint uses multipart form data because file uploads require a different format from normal JSON.

Frontend logic:

```javascript
const formData = new FormData();
formData.append("file", file);
```

## What Is JSON?

JSON stands for JavaScript Object Notation. It is a lightweight data format used for exchanging data between systems.

JSON looks like this:

```json
{
  "name": "Document Review Platform",
  "status": "running"
}
```

It is easy for JavaScript to parse and easy for humans to read.

## Why JSON Is Used In This Project

JSON is used because:

- FastAPI supports JSON naturally.
- JavaScript can read JSON easily.
- It is common in REST APIs.
- It is structured.
- It works well for dashboard output.

The backend sends JSON, and the frontend converts it into UI cards.

## Response Structure

The main response has five top-level fields:

| Field | Meaning |
| --- | --- |
| `summary` | Short summary of the document |
| `key_entities` | Extracted organizations, dates, amounts, invoice IDs |
| `risk_flags` | Risk terms detected in the document |
| `action_items` | Recommended next steps |
| `confidence_score` | Rule-based quality indicator |

## Key Entities JSON

`key_entities` is a nested object:

```json
{
  "organizations": ["ABC Ltd"],
  "dates": ["1 April 2026"],
  "amounts": ["$7,500"],
  "invoice_ids": ["INV-20431"]
}
```

This structure is useful because the frontend can separately render each category.

## Error Responses

APIs should return useful error messages when something goes wrong.

Examples:

### Empty Text

Status code:

```text
400 Bad Request
```

Response:

```json
{
  "detail": "Text input cannot be empty"
}
```

### Unsupported File

Status code:

```text
400 Bad Request
```

Response:

```json
{
  "detail": "Only .txt files are supported"
}
```

### Unexpected Backend Error

Status code:

```text
500 Internal Server Error
```

Response:

```json
{
  "detail": "Error analyzing text: ..."
}
```

## Status Codes To Know

| Status Code | Meaning | Project Example |
| --- | --- | --- |
| 200 | Success | Analysis completed |
| 400 | Bad request | Empty text or wrong file type |
| 404 | Not found | Wrong endpoint URL |
| 422 | Validation error | Invalid request schema |
| 500 | Server error | Unexpected backend failure |

## How JavaScript Handles API Responses

JavaScript sends the request using `fetch`.

Then it checks:

```javascript
if (!response.ok) {
  throw new Error(...)
}
```

If successful:

```javascript
const data = await response.json();
renderResults(data);
```

This means the frontend converts the backend JSON response into visible dashboard content.

## FastAPI Automatic Docs

FastAPI provides automatic API documentation at:

```text
http://127.0.0.1:8000/docs
```

This page lets you:

- View endpoints.
- See request schemas.
- See response schemas.
- Test API calls from the browser.

Interview answer:

> FastAPI's automatic docs were useful because they allowed me to test backend endpoints directly and clearly show the API contract during development.

## API Contract

An API contract means the agreed structure of requests and responses.

For this project:

- Frontend agrees to send `{ "text": "..." }` for pasted text.
- Backend agrees to return `summary`, `key_entities`, `risk_flags`, `action_items`, and `confidence_score`.

Why this matters:

- Frontend and backend remain compatible.
- Bugs are easier to find.
- Future developers understand the data format.

## Strong Interview Answer

> The frontend communicates with the backend through REST API endpoints. For pasted text, it sends a POST request to `/analyze-text` with a JSON body containing the document text. For file upload, it sends multipart form data to `/upload-document`. FastAPI validates the request using Pydantic, runs the analysis pipeline, and returns a structured JSON response with summary, entities, risk flags, action items, and confidence score. JavaScript then parses the JSON and updates the dashboard.

## Interview Tip

When explaining APIs, use one concrete endpoint example. For this project, `POST /analyze-text` is the best example.

## Common Mistakes

- Saying GET is used to send document text.
- Forgetting that file upload uses `FormData`, not JSON.
- Not knowing what JSON stands for.
- Ignoring status codes.
- Saying the frontend receives plain text only. It receives structured JSON.

## 5 Rapid Fire Questions

1. What is an API?
2. What is JSON?
3. Why is POST used for analysis?
4. What does `/health` return?
5. What are the main fields in the API response?

## 30 Second Revision Summary

The project uses REST APIs to connect the JavaScript frontend with the FastAPI backend. GET endpoints check server status, while POST endpoints send document text or uploaded files for analysis. The backend returns JSON containing summary, key entities, risk flags, action items, and confidence score. The frontend parses this JSON and displays it in dashboard cards.
