# 12 Interview Q&A Project

## How To Use This File

This file contains 100 interview questions and sample answers for the AI-Powered Document Review & Risk Insights Platform.

Use it for:

- Internship interviews
- Viva/oral rounds
- Resume project explanation
- Technical HR rounds
- Project presentation preparation
- Quick revision before interviews

Best strategy:

1. Learn the first 15 basic answers very well.
2. Practice the technical and NLP sections using your own words.
3. Memorize the business value answers for consulting, audit, finance, and KPMG-style interviews.
4. Use the advanced answers to show future thinking.

## Basic Project Questions

### 1. Explain your project.

**Answer:**  
My project is an AI-Powered Document Review & Risk Insights Platform. It helps business teams analyze documents such as contracts, invoices, audit notes, policy documents, and compliance memos. Users can paste text or upload a `.txt` file. The backend summarizes the document, extracts important entities like organizations, dates, amounts, and invoice IDs, detects risk keywords such as penalty, overdue, breach, liability, fraud, and dispute, and generates recommended action items. The result is shown on a frontend dashboard as structured business insights.

### 2. Why did you build this project?

**Answer:**  
I built it because manual document review is slow, repetitive, and error-prone. Business teams spend a lot of time reading long documents to find key details and risk terms. This project automates the first-pass review so users can understand the document faster and focus on decision-making.

### 3. What problem does the project solve?

**Answer:**  
It solves document review inefficiency. It converts unstructured business text into structured output: summary, entities, risk flags, action items, and confidence score. This helps teams reduce manual reading time and avoid missing important details.

### 4. Who are the target users?

**Answer:**  
The target users are consulting analysts, audit teams, finance teams, compliance officers, procurement teams, and operations teams. These users regularly handle contracts, invoices, vendor agreements, audit notes, and internal memos.

### 5. What are the main features?

**Answer:**  
The main features are pasted text analysis, `.txt` file upload, document summarization, entity extraction, risk keyword detection, action item generation, confidence scoring, and dashboard-based result display.

### 6. What type of documents can it analyze?

**Answer:**  
It can analyze text-based business documents such as contracts, invoices, vendor agreements, audit reports, compliance notes, policy documents, meeting minutes, and internal memos. Currently it supports pasted text and `.txt` files.

### 7. What output does the system generate?

**Answer:**  
The system generates a structured JSON response containing summary, key entities, risk flags, action items, and confidence score. The frontend displays these results in separate cards.

### 8. What makes your project different from a simple summarizer?

**Answer:**  
A simple summarizer only shortens text. My project also extracts business entities, detects risk terms, generates recommended actions, and presents the output in a dashboard. It is designed for business review, not just text shortening.

### 9. Is this project replacing human reviewers?

**Answer:**  
No. It supports human reviewers by automating the first-pass review. Final decisions should still be made by professionals, especially for legal, audit, or compliance matters.

### 10. What is the most important benefit of the project?

**Answer:**  
The most important benefit is faster and more consistent document review. Users can quickly understand long documents and identify important risk terms without manually scanning every line.

### 11. What is the complete user flow?

**Answer:**  
The user pastes text or uploads a `.txt` file, clicks Analyze Document, the frontend sends the input to the FastAPI backend, the backend runs the NLP pipeline, returns JSON insights, and the frontend displays summary, entities, risks, actions, and confidence score.

### 12. What is the project title and how would you describe it in one line?

**Answer:**  
The title is AI-Powered Document Review & Risk Insights Platform. In one line: it converts business documents into summaries, extracted details, risk alerts, and recommended actions.

### 13. What was your main learning from this project?

**Answer:**  
I learned how to connect backend APIs, NLP logic, and frontend visualization into one practical business application. I also learned the importance of modular architecture and explainable business logic.

### 14. Why is this a good internship project?

**Answer:**  
It is a good internship project because it shows full-stack development, API design, NLP concepts, business problem solving, documentation, and future scalability. It is practical and easy to connect with real company workflows.

### 15. How would you explain it to a non-technical person?

**Answer:**  
It is a tool that reads business documents and gives a quick report. It tells you what the document is about, what important names, dates, and amounts are present, what risk words appear, and what actions should be taken next.

## Technical Questions

### 16. What tech stack did you use?

**Answer:**  
I used Python and FastAPI for the backend, Pydantic for validation, HTML/CSS/JavaScript for the frontend, regex for pattern extraction, optional spaCy for entity recognition, optional transformers for summarization, and Git/GitHub for version control.

### 17. Why did you choose Python?

**Answer:**  
Python is strong for NLP and backend development. It has useful libraries for text processing, regex, spaCy, transformers, FastAPI, and testing. It also keeps the code readable and suitable for rapid development.

### 18. Why did you use FastAPI?

**Answer:**  
FastAPI is modern, fast, and ideal for JSON APIs. It supports automatic documentation, request validation with Pydantic, clean route definitions, and strong performance. It fit the project because the frontend needed to call backend endpoints.

### 19. Why FastAPI instead of Flask?

**Answer:**  
Flask is good, but FastAPI provides built-in request validation, automatic Swagger docs, better type-hint support, and a more API-focused development style. Since this project depends on structured JSON APIs, FastAPI was a better fit.

### 20. What is Pydantic used for?

**Answer:**  
Pydantic is used to define and validate request and response schemas. In this project, it ensures the text input and document analysis response follow a predictable structure.

### 21. What is the role of `backend/main.py`?

**Answer:**  
`backend/main.py` creates the FastAPI app, sets title and description, configures CORS, includes the API router, and defines the root endpoint.

### 22. What is the role of `routes.py`?

**Answer:**  
`routes.py` defines the API endpoints. It handles health checks, pasted text analysis, file upload analysis, input validation, error handling, and calls the pipeline service.

### 23. What is the role of `pipeline_service.py`?

**Answer:**  
`pipeline_service.py` orchestrates the full document analysis workflow. It sanitizes text, normalizes it, summarizes it, extracts entities, detects risks, generates action items, calculates confidence, and returns structured output.

### 24. What is the role of `nlp_service.py`?

**Answer:**  
`nlp_service.py` contains the main NLP and business logic functions: summarization, entity extraction, risk detection, and action item generation.

### 25. What is CORS and why did you configure it?

**Answer:**  
CORS stands for Cross-Origin Resource Sharing. It allows the browser frontend running on one origin, such as `localhost:5500`, to call the backend running on another origin, such as `localhost:8000`. Without CORS, the browser may block API calls.

### 26. What is an API endpoint?

**Answer:**  
An API endpoint is a specific URL and HTTP method that performs a backend action. For example, `POST /analyze-text` receives document text and returns analysis results.

### 27. What endpoints does your project have?

**Answer:**  
The project has `/` for root status, `/health` for health check, `/analyze-text` for pasted text analysis, and `/upload-document` for `.txt` file upload analysis.

### 28. Why did you use POST for document analysis?

**Answer:**  
POST is used because the frontend sends document content to the backend. POST supports request bodies and is suitable for processing submitted data, while GET is mainly for retrieving data.

### 29. What is JSON?

**Answer:**  
JSON stands for JavaScript Object Notation. It is a lightweight structured data format used for communication between frontend and backend.

### 30. Why does the backend return JSON?

**Answer:**  
The backend returns JSON because it is easy for JavaScript to parse and display. It also keeps the response structured with fields like summary, entities, risks, actions, and confidence.

### 31. How does the frontend call the backend?

**Answer:**  
The frontend uses JavaScript's `fetch` API. For pasted text, it sends a JSON POST request to `/analyze-text`. For files, it sends `FormData` to `/upload-document`.

### 32. What is the Fetch API?

**Answer:**  
The Fetch API is a browser feature used to make HTTP requests from JavaScript. In this project, it sends document input to the backend and receives JSON results.

### 33. What is `FormData` used for?

**Answer:**  
`FormData` is used to send uploaded files from the frontend to the backend using multipart form data. It is used for the `.txt` file upload endpoint.

### 34. What happens if the user submits empty text?

**Answer:**  
The backend raises a 400 Bad Request error with a message saying the text input cannot be empty. The frontend displays the error message to the user.

### 35. What happens if the user uploads a non-`.txt` file?

**Answer:**  
The backend rejects it with a 400 Bad Request error because the current version only supports `.txt` files.

### 36. Why only `.txt` files in the current version?

**Answer:**  
The first version focuses on the core NLP and API pipeline using plain text. PDF, DOCX, and OCR support are planned future improvements.

### 37. What is schema validation?

**Answer:**  
Schema validation checks that input and output data follow expected fields and types. It prevents unexpected data from breaking the system.

### 38. What is the response schema?

**Answer:**  
The response schema includes `summary`, `key_entities`, `risk_flags`, `action_items`, and `confidence_score`.

### 39. What is the frontend built with?

**Answer:**  
The frontend is built with HTML for structure, CSS for design, and JavaScript for interactivity and API calls.

### 40. Why did you not use React?

**Answer:**  
The project has one main dashboard screen and limited state management needs, so plain JavaScript was enough. React could be added later if the app grows into a larger multi-page dashboard.

### 41. What does `index.html` contain?

**Answer:**  
It contains the page structure: header, input card, tabs, textarea, file upload control, analyze button, error/status areas, and result cards.

### 42. What does `styles.css` do?

**Answer:**  
It controls the visual design, including layout, colors, cards, tabs, buttons, chips, responsive behavior, loading spinner, and error styling.

### 43. What does `app.js` do?

**Answer:**  
It handles tab switching, sample text insertion, file selection, input validation, fetch API calls, loading states, error messages, and rendering backend results.

### 44. How are results displayed in the UI?

**Answer:**  
JavaScript receives JSON from the backend and updates DOM elements. Summary is shown as text, entities as chips, risks and actions as lists, and confidence as a badge.

### 45. Why is modular architecture important?

**Answer:**  
Modular architecture keeps responsibilities separate. Routes handle HTTP, services handle processing, schemas handle validation, utilities handle reusable helpers, and frontend files handle UI. This improves readability, testing, debugging, and future extension.

## NLP And Pipeline Questions

### 46. What is NLP?

**Answer:**  
NLP stands for Natural Language Processing. It helps computers process human language. In this project, NLP is used to summarize documents, extract key information, detect risk words, and generate action items.

### 47. What NLP tasks are used in your project?

**Answer:**  
The project uses text cleaning, summarization, entity extraction, keyword-based risk detection, regex extraction, and rule-based action generation.

### 48. What is summarization?

**Answer:**  
Summarization creates a shorter version of a long text while preserving the main meaning. It helps users quickly understand business documents.

### 49. How does summarization work in your project?

**Answer:**  
The project can use transformer-based summarization if available. If not, it falls back to a simpler summary using the first few sentences. This makes the app more reliable during local demos.

### 50. Why did you include fallback summarization?

**Answer:**  
Transformer models can be heavy or unavailable in some environments. Fallback summarization ensures the app still produces useful output instead of failing completely.

### 51. What is entity extraction?

**Answer:**  
Entity extraction identifies important values in text, such as organization names, dates, amounts, and invoice IDs.

### 52. Which entities does your system extract?

**Answer:**  
It extracts organizations, dates, amounts, and invoice IDs.

### 53. Why are entities useful?

**Answer:**  
Entities give exact business details. A summary tells the topic, but entities tell who is involved, what amount is mentioned, which date matters, and which invoice is affected.

### 54. What is regex?

**Answer:**  
Regex, or regular expression, is a pattern-matching method used to find specific text formats such as dates, amounts, invoice IDs, emails, and phone numbers.

### 55. Why is regex useful in this project?

**Answer:**  
Business documents often contain predictable patterns like invoice IDs and currency amounts. Regex is fast and explainable for extracting these values.

### 56. What is Named Entity Recognition?

**Answer:**  
Named Entity Recognition is an NLP task that identifies real-world entities in text, such as organizations, dates, people, locations, and monetary values.

### 57. How is spaCy used?

**Answer:**  
spaCy is optional in the project. If available, it helps identify organization entities. If it is not available, the system still works using regex-based fallback logic.

### 58. What is risk detection?

**Answer:**  
Risk detection scans the document for predefined business risk keywords such as penalty, overdue, breach, liability, urgent, fraud, dispute, and non-compliance.

### 59. How does your risk detection logic work?

**Answer:**  
The text is converted to lowercase, then the system checks whether each predefined risk keyword appears in the document. Matching keywords are deduplicated and returned as risk flags.

### 60. Why did you use keyword-based risk detection?

**Answer:**  
Keyword detection is fast, explainable, and does not require a labeled dataset. It is a practical version 1 approach for known business risk terms.

### 61. What are the limitations of keyword detection?

**Answer:**  
It may produce false positives, miss synonyms, and fail to understand context or negation. For example, "no penalty applies" may still be flagged because the word penalty appears.

### 62. What is a false positive?

**Answer:**  
A false positive occurs when the system flags a risk even though there is no actual risk in context.

### 63. What is a false negative?

**Answer:**  
A false negative occurs when the system misses a real risk because the wording does not match the predefined keywords.

### 64. How are action items generated?

**Answer:**  
Action items are generated using rule-based mapping. For example, if `penalty` is detected, the system recommends reviewing penalty clauses. If `overdue` is detected, it recommends following up on payment.

### 65. Why are action items important?

**Answer:**  
They make the output practical. Instead of only showing detected words, the system tells the user what to review or do next.

### 66. What is the confidence score?

**Answer:**  
The confidence score is a rule-based indicator based on whether the system found a summary, entities, and risk flags. It is not a machine learning probability.

### 67. How is confidence calculated?

**Answer:**  
The backend adds points for available summary, detected organizations, dates, amounts, invoice IDs, and risks. Based on the score, it returns High, Medium, or Low.

### 68. Why do you sanitize text?

**Answer:**  
Sanitization masks sensitive values like emails, phone numbers, and bank identifiers. This shows privacy awareness when handling business documents.

### 69. What is text normalization?

**Answer:**  
Text normalization cleans the input by trimming spaces and converting multiple spaces or line breaks into consistent spacing. It improves downstream processing.

### 70. What is the complete NLP pipeline?

**Answer:**  
The pipeline is: input text, privacy sanitization, text normalization, summarization, entity extraction, risk detection, action item generation, confidence scoring, JSON response, and frontend display.

## Business Questions

### 71. How is this useful for KPMG?

**Answer:**  
KPMG and similar consulting firms work with audits, compliance reviews, contracts, process documents, and client reports. This platform can speed up first-pass document review, highlight risk language, and produce structured insights for analysts.

### 72. How is it useful for consulting teams?

**Answer:**  
Consulting teams often review large client documents and convert them into findings. This tool helps summarize documents, extract important details, and identify risks faster.

### 73. How is it useful for finance teams?

**Answer:**  
Finance teams can use it to detect overdue invoices, payment amounts, invoice IDs, penalty terms, and disputes. It helps prioritize follow-up and payment tracking.

### 74. How is it useful for audit teams?

**Answer:**  
Audit teams can use it to summarize audit notes, detect non-compliance or breach language, and generate follow-up action items for remediation.

### 75. How is it useful for operations teams?

**Answer:**  
Operations teams can use it to review vendor agreements, delivery delays, escalation notes, and internal memos. It helps them identify urgent operational issues.

### 76. What is the business value?

**Answer:**  
The business value is faster review, improved consistency, reduced missed details, better risk visibility, and more actionable reporting.

### 77. How does it reduce errors?

**Answer:**  
It applies the same risk and extraction logic every time, reducing dependence on human memory and manual scanning.

### 78. How does it save time?

**Answer:**  
It gives a quick summary and extracts important values automatically, so users do not need to read the full document before understanding the main points.

### 79. How does it improve scalability?

**Answer:**  
The same pipeline can process many documents. New rules, document types, and output fields can be added without redesigning the whole system.

### 80. What kind of companies would use this?

**Answer:**  
Consulting firms, audit firms, banks, finance departments, compliance teams, legal operations teams, procurement teams, and large enterprises with document-heavy workflows.

### 81. What is the ROI idea behind this project?

**Answer:**  
The ROI comes from reducing analyst time, improving review consistency, catching risks earlier, and creating structured reports faster.

### 82. Why is this better than manual review only?

**Answer:**  
Manual review is still important, but automation speeds up the first pass and highlights what needs attention. It helps humans focus on judgment instead of repetitive scanning.

## HR And Behavioral Questions

### 83. What was the biggest challenge?

**Answer:**  
The biggest challenge was designing the system so it was practical and explainable. I had to balance NLP features with reliability, so I used a modular pipeline with fallback logic instead of depending only on heavy models.

### 84. How did you handle errors?

**Answer:**  
I handled errors using validation and HTTP exceptions. Empty text, unsupported files, and empty uploads return clear 400 errors, while unexpected backend failures return 500 errors.

### 85. What would you improve if you had more time?

**Answer:**  
I would add PDF parsing, OCR for scanned documents, user login, database storage, saved report history, analytics dashboard, LLM-based summaries, risk severity scoring, and cloud deployment.

### 86. What did this project teach you about real-world software?

**Answer:**  
It taught me that real applications need more than algorithms. They need clean architecture, input validation, error handling, user-friendly design, and business value.

### 87. How did you decide the features?

**Answer:**  
I chose features based on common business document review needs: summary for quick understanding, entities for key details, risk flags for warning signals, and action items for next steps.

### 88. What is your favorite part of the project?

**Answer:**  
My favorite part is the end-to-end pipeline because it connects a real business problem with technical implementation. The user submits a document and receives structured insights that are actually useful.

### 89. What would you say if the interviewer says the project is simple?

**Answer:**  
I would say the first version is intentionally simple and explainable. It focuses on building a complete working system with clean architecture. The design can be extended with ML risk classification, LLM summarization, database storage, and enterprise security.

### 90. How does this project show teamwork readiness?

**Answer:**  
The modular structure makes it easier for different developers to work on frontend, backend, NLP services, and database features separately. This shows awareness of maintainable team development.

## Advanced Questions

### 91. How would you scale this application?

**Answer:**  
I would deploy the backend with multiple workers, add background queues for large documents, store reports in a database, cache repeated results, use cloud storage for files, and separate heavy model inference into a dedicated service if needed.

### 92. How would you add authentication?

**Answer:**  
I would add user registration and login using JWT-based authentication or session-based authentication. Users would have roles such as analyst, manager, and admin.

### 93. How would you add role-based access?

**Answer:**  
I would store user roles in a database and check permissions before allowing actions. For example, analysts can upload documents, managers can view team reports, and admins can manage users.

### 94. How would you add a database?

**Answer:**  
I would store users, documents, reports, risk flags, action items, and logs. MongoDB would work well for flexible JSON reports, while MySQL would work well for structured relational data.

### 95. How would you support PDF files?

**Answer:**  
I would use a PDF parsing library to extract text from digital PDFs. For scanned PDFs, I would add OCR to convert images into text before sending it to the pipeline.

### 96. How would you improve risk detection?

**Answer:**  
I would add phrase matching, negation handling, synonym lists, sentence-level classification, risk categories, severity scoring, and possibly an ML or LLM-based classifier trained on labeled business documents.

### 97. How would you handle privacy in production?

**Answer:**  
I would add authentication, encryption, file size limits, access control, secure storage, audit logs, data retention policies, HTTPS, and careful logging that avoids exposing sensitive document content.

### 98. How would you deploy this project?

**Answer:**  
The FastAPI backend could be deployed on Render, Railway, Azure, AWS, or similar platforms. The frontend could be hosted as a static site. Environment variables would manage configuration, and CORS would be updated for production domains.

### 99. How would you test this project?

**Answer:**  
I would test API endpoints, pipeline functions, entity extraction patterns, risk detection, action item generation, error handling, and frontend behavior. Unit tests can check individual functions, while integration tests can check the full API flow.

### 100. What is the strongest technical point of your project?

**Answer:**  
The strongest technical point is the end-to-end architecture. It is not just an isolated NLP script. It has a frontend dashboard, FastAPI backend, schema validation, modular services, a document processing pipeline, and structured JSON output.

## Bonus: Best Answers To Memorize

### Best 30-Second Project Explanation

> I built an AI-Powered Document Review and Risk Insights Platform that helps business teams analyze contracts, invoices, audit notes, and compliance documents. Users paste text or upload a `.txt` file, and the FastAPI backend runs an NLP pipeline to summarize the document, extract organizations, dates, amounts, and invoice IDs, detect risk keywords, generate action items, and return a confidence score. The JavaScript frontend displays the result in dashboard cards. The main value is faster, more consistent first-pass document review.

### Best Technical Architecture Answer

> The frontend uses HTML, CSS, and JavaScript. JavaScript sends API requests to a FastAPI backend. The backend routes validate input using Pydantic schemas and call the pipeline service. The pipeline sanitizes and normalizes text, then calls NLP functions for summarization, entity extraction, risk detection, and action generation. The backend returns a structured JSON response, and the frontend renders it in cards.

### Best Business Value Answer

> The business value is that it reduces manual document review time, improves consistency, and helps teams detect important risk indicators early. It is useful for consulting, finance, audit, compliance, and operations teams because these teams handle large volumes of document-heavy work.

## Interview Tip

For any question, answer in this order: what it is, how it works in your project, why it matters, and one limitation or future improvement if relevant.

## Common Mistakes

- Memorizing only definitions without connecting them to the project.
- Saying the project gives final legal decisions.
- Forgetting the frontend-backend flow.
- Calling the confidence score an ML probability.
- Not being able to explain why FastAPI, JSON, regex, or POST were used.

## 5 Rapid Fire Questions

1. Explain the project in one sentence.
2. What does the backend return?
3. Why is FastAPI used?
4. What are the main NLP tasks?
5. What is the biggest future improvement?

## 30 Second Revision Summary

This project is a full-stack business document intelligence platform. It uses a JavaScript frontend and FastAPI backend to process pasted text or uploaded `.txt` files. The NLP pipeline cleans text, summarizes it, extracts entities, detects risk keywords, generates action items, and returns JSON. The strongest interview points are business value, modular architecture, explainable NLP logic, and clear future scope.
