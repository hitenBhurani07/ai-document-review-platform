# 02 Tech Stack Deep Dive

## Purpose Of This File

This file explains every major technology used in the AI-Powered Document Review & Risk Insights Platform. The goal is to help you answer interview questions confidently, even if the interviewer asks basic, practical, or comparison-based questions.

The project uses:

- **Python** for backend and NLP logic.
- **FastAPI** for building REST APIs.
- **Pydantic** for request and response validation.
- **HTML** for page structure.
- **CSS** for styling and responsive layout.
- **JavaScript** for frontend interactivity and API calls.
- **spaCy** as an optional NLP library for entity recognition.
- **Regex** for pattern-based extraction and risk detection.
- **Transformers** as an optional summarization approach.
- **Git and GitHub** for version control and portfolio presentation.

## High-Level Stack

| Layer | Technology | Purpose |
| --- | --- | --- |
| Frontend | HTML, CSS, JavaScript | User dashboard for input and results |
| API backend | FastAPI | Receives document input and returns insights |
| Validation | Pydantic | Defines request and response structure |
| NLP logic | Python, regex, optional spaCy, optional transformers | Summarization, extraction, risk detection |
| Utilities | Python helper modules | Text cleaning, privacy masking, report formatting |
| Version control | Git, GitHub | Track changes and show project professionally |

## Backend Technology

## Python

### What Is Python?

Python is a high-level programming language known for readability and a strong ecosystem of libraries. It is widely used in backend development, automation, data science, machine learning, and NLP.

### Beginner Explanation

Python is like a simple and readable language for giving instructions to a computer. In this project, Python tells the system how to:

- Clean text.
- Summarize documents.
- Extract important values.
- Detect risk words.
- Generate actions.
- Return a structured result.

### Why Python Was Used

Python is a strong choice for this project because NLP and business text processing are easier in Python than in many other languages.

Key reasons:

- It has excellent NLP libraries.
- It supports regex for text pattern extraction.
- It works well with FastAPI.
- It is beginner-friendly and interview-friendly.
- It is commonly used in AI, automation, and data projects.

### Why Python Instead Of Java Or C++?

Java and C++ are powerful, but Python is usually faster for building NLP prototypes.

| Language | Strength | Why Python Is Better Here |
| --- | --- | --- |
| Java | Enterprise backend systems | More code needed for text processing prototypes |
| C++ | Performance-heavy systems | Too complex for a lightweight NLP web app |
| Python | AI, NLP, APIs, automation | Best balance of speed, libraries, and readability |

### How Python Is Used In This Project

Python is used in:

- `backend/main.py` for creating the FastAPI app.
- `backend/api/routes.py` for API endpoints.
- `backend/services/pipeline_service.py` for orchestration.
- `backend/services/nlp_service.py` for summarization, extraction, risk detection, and action generation.
- `utils/text_utils.py` for text normalization.
- `utils/privacy.py` for masking sensitive information.

### Interview Questions On Python

**Q: Why did you choose Python for this project?**  
A: I chose Python because it has strong support for NLP and backend development. Libraries like regex, spaCy, transformers, and FastAPI make it easy to build a text analysis system quickly while keeping the code readable and modular.

**Q: Is Python scalable enough for this type of project?**  
A: Yes, for an API-based NLP application Python is practical. Scaling can be handled using async endpoints, background queues, caching, multiple workers, and cloud deployment. Heavy model inference can also be separated into a dedicated service.

## FastAPI

### What Is FastAPI?

FastAPI is a modern Python framework for building APIs. It allows developers to create endpoints such as:

- `GET /health`
- `POST /analyze-text`
- `POST /upload-document`

An API endpoint is a URL that the frontend can call to send or receive data.

### Beginner Explanation

FastAPI acts like the waiter between the frontend and the backend logic.

- The frontend says: "Here is a document."
- FastAPI receives it.
- FastAPI sends it to the pipeline.
- The pipeline analyzes it.
- FastAPI returns the result as JSON.

### Why FastAPI Was Used

FastAPI was used because it is:

- Fast and lightweight.
- Easy to write.
- Good for JSON APIs.
- Built with automatic validation support.
- Able to generate interactive API docs at `/docs`.
- Popular in modern Python backend development.

### How FastAPI Is Used In This Project

In `backend/main.py`, the project creates a FastAPI application:

```python
app = FastAPI(
    title="AI-Powered Document Review & Risk Insights Platform",
    version="1.0.0",
)
```

The app includes routes from `backend/api/routes.py`. The project has endpoints for:

- Checking server health.
- Analyzing pasted text.
- Uploading and analyzing a `.txt` file.

### Why FastAPI Instead Of Flask?

This is a common interview question.

| Feature | Flask | FastAPI |
| --- | --- | --- |
| Type validation | Manual or extension-based | Built in with Pydantic |
| API docs | Need extension | Automatic `/docs` |
| Async support | Possible but not the original focus | Designed for modern async APIs |
| Request models | Manual | Clean schema classes |
| Interview value | Good | More modern API-focused choice |

Strong answer:

> I used FastAPI because this project is API-centered. FastAPI gives automatic documentation, request validation with Pydantic, clean route definitions, and strong performance. Flask is also good, but FastAPI was a better fit for a structured JSON API that needs validation and clear API documentation.

### Interview Questions On FastAPI

**Q: What is an endpoint?**  
A: An endpoint is a specific URL and HTTP method combination that performs an action. For example, `POST /analyze-text` receives document text and returns analysis results.

**Q: What is the use of `/docs` in FastAPI?**  
A: FastAPI automatically generates Swagger UI documentation at `/docs`, where we can test API endpoints directly in the browser.

**Q: What is CORS?**  
A: CORS stands for Cross-Origin Resource Sharing. It controls whether a frontend running on one address, like `localhost:5500`, can call a backend running on another address, like `localhost:8000`.

## Pydantic

### What Is Pydantic?

Pydantic is a Python library used for data validation. FastAPI uses it to define what request data should look like and what response data should look like.

### How It Is Used

The project has schemas in `backend/schemas/document.py`:

- `DocumentRequest` defines the input text.
- `EntityBlock` defines entity categories.
- `DocumentResponse` defines the structured output.

Example response structure:

```json
{
  "summary": "Short document summary",
  "key_entities": {
    "organizations": [],
    "dates": [],
    "amounts": [],
    "invoice_ids": []
  },
  "risk_flags": [],
  "action_items": [],
  "confidence_score": "Medium"
}
```

### Why Pydantic Helps

Without validation, the backend may receive unexpected data. Pydantic helps by:

- Checking required fields.
- Keeping responses consistent.
- Improving API documentation.
- Reducing runtime errors.

### Interview Answer

> Pydantic helps define the contract between frontend and backend. It ensures the request contains valid text and the response follows a predictable structure with summary, entities, risks, actions, and confidence score.

## Frontend Technology

## HTML

### What Is HTML?

HTML stands for HyperText Markup Language. It defines the structure of a webpage.

### Beginner Explanation

HTML is the skeleton of the page. It decides which elements exist:

- Header
- Textarea
- File input
- Buttons
- Result cards
- Lists
- Status messages

### How HTML Is Used

The project uses `frontend/index.html` to create:

- A navigation/header area.
- A hero section explaining the product.
- Tabs for pasted text and file upload.
- A textarea for document input.
- A file picker for `.txt` uploads.
- A button to analyze the document.
- Result cards for summary, entities, risks, actions, and confidence.

### Interview Question

**Q: What role does HTML play in your project?**  
A: HTML defines the frontend structure. It creates the input form, file upload area, analyze button, and output sections where API results are displayed.

## CSS

### What Is CSS?

CSS stands for Cascading Style Sheets. It controls how the webpage looks.

### How CSS Is Used

The project uses `frontend/styles.css` for:

- Layout
- Colors
- Cards
- Buttons
- Tabs
- Responsive behavior
- Status and error styling
- Loading spinner

The design uses a dashboard style because the target users are business professionals. Results are shown in clear cards, making the output easy to scan.

### Why CSS Matters

For interview projects, UI quality matters because it shows product thinking. A good frontend makes the technical work understandable to non-technical users.

### Interview Question

**Q: Why did you use cards in the UI?**  
A: Cards separate different categories of output. Summary, entities, risks, actions, and confidence are different types of information, so cards make the dashboard easier to read.

## JavaScript

### What Is JavaScript?

JavaScript is the programming language used in the browser to make pages interactive.

### Beginner Explanation

HTML displays the page. CSS styles it. JavaScript makes it respond to user actions.

In this project, JavaScript handles:

- Switching between paste-text and upload-file tabs.
- Inserting sample text.
- Reading the selected file name.
- Sending API requests with `fetch`.
- Showing loading status.
- Rendering JSON results into the UI.
- Showing error messages.

### Why JavaScript Was Used

JavaScript was used because it runs directly in the browser. It allows the frontend to communicate with the FastAPI backend without reloading the page.

### How It Talks To Backend

For pasted text:

```javascript
fetch("http://127.0.0.1:8000/analyze-text", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ text })
});
```

For file upload:

```javascript
const formData = new FormData();
formData.append("file", file);
fetch("http://127.0.0.1:8000/upload-document", {
  method: "POST",
  body: formData
});
```

### Interview Question

**Q: Why did you use JavaScript instead of a framework like React?**  
A: The project frontend is focused and lightweight. Plain JavaScript is enough for form handling, API calls, and DOM updates. React would be useful later if the dashboard grows into a larger application with many pages and reusable components.

## NLP And Text Processing Technologies

## Regex

### What Is Regex?

Regex means regular expression. It is a pattern-matching technique used to find specific text formats.

### Beginner Explanation

Regex is like a search rule. Instead of searching only one exact word, regex can search for patterns such as:

- Dates like `2026-04-29`
- Amounts like `$7,500`
- Invoice IDs like `INV-20431`
- Email addresses
- Phone numbers

### How Regex Is Used

The project uses regex for:

- Dates
- Amounts
- Invoice IDs
- Organization-like names
- Email masking
- Phone masking
- Bank identifier masking

### Why Regex Is Useful

Regex is useful because business documents often contain predictable formats. For example, invoices frequently use IDs like `INV-12345`, and amounts often include currency symbols.

### Limitation

Regex is not intelligent by itself. It finds patterns, but it does not understand meaning deeply. That is why future improvements may use ML models or LLMs.

### Interview Question

**Q: Why is regex useful in this project?**  
A: Regex is useful for extracting structured patterns from unstructured text, such as dates, amounts, invoice IDs, emails, and phone numbers. It is fast, explainable, and works well for predictable business formats.

## spaCy

### What Is spaCy?

spaCy is a popular Python NLP library. It can perform tokenization, sentence splitting, and named entity recognition.

### How It Is Used

In this project, spaCy is optional. If available, the backend tries to load an English model and use it to detect organizations. If the model is not available, the project still works using fallback logic.

### Why Optional?

Making spaCy optional keeps the project practical. The system should not fail completely just because a model is missing. This shows good engineering judgment.

### Interview Question

**Q: What is Named Entity Recognition?**  
A: Named Entity Recognition, or NER, is the process of identifying real-world entities in text, such as organizations, dates, people, locations, and monetary values. In this project, it helps identify organizations in business documents.

## Transformers

### What Are Transformers?

Transformers are modern deep learning models used for language tasks such as summarization, translation, question answering, and text generation.

### How They Are Used

The project includes transformer-based summarization support using Hugging Face. The summarizer is configured around `facebook/bart-large-cnn`. If transformer summarization is not available, the project falls back to a simple first-few-sentences summary.

### Why This Is Practical

This design is useful because:

- The project can use advanced summarization when available.
- The app still works without heavy model dependencies.
- The fallback makes local testing easier.

### Interview Question

**Q: Why did you include a fallback summary?**  
A: Transformer models can be heavy and may fail if dependencies or models are unavailable. The fallback summary ensures the application remains usable and reliable during local development or demos.

## Git

### What Is Git?

Git is a version control system. It tracks changes in code over time.

### Why Git Is Useful

Git helps developers:

- Track project history.
- Compare changes.
- Revert mistakes if needed.
- Work on features safely.
- Prepare code for GitHub.

### Interview Question

**Q: Why is version control important?**  
A: Version control keeps a history of changes, helps manage project evolution, and makes collaboration easier. It also shows recruiters that the project was developed professionally.

## GitHub

### What Is GitHub?

GitHub is a platform for hosting Git repositories online. It is used for collaboration, portfolio building, issue tracking, and project presentation.

### Why GitHub Matters For This Project

For interviews, GitHub is important because it shows:

- Code structure
- Documentation
- Commit history
- README quality
- Project completeness
- Deployment readiness

### Interview Question

**Q: What should a good GitHub project include?**  
A: It should include a clear README, setup instructions, project architecture, screenshots if possible, example inputs and outputs, dependency information, and clean folder structure.

## Why This Stack Works Well Together

The technologies form a simple but powerful architecture:

```text
HTML/CSS/JavaScript frontend
        |
        v
FastAPI backend
        |
        v
Python NLP pipeline
        |
        v
JSON response
        |
        v
Dashboard cards
```

This stack is good for an internship project because it shows full-stack ability without unnecessary complexity.

## Strong Interview Summary

> The project uses a lightweight full-stack architecture. The frontend is built with HTML, CSS, and JavaScript for a simple business dashboard. JavaScript sends requests to a FastAPI backend. FastAPI validates requests using Pydantic and passes the document text to a Python NLP pipeline. The NLP layer uses text cleaning, regex, optional spaCy, and optional transformer summarization to produce structured JSON insights. Git and GitHub support version control and portfolio presentation.

## Interview Tip

When asked about technology choices, always connect the tool to the project need. Do not just say "I used FastAPI because it is fast." Say "I used FastAPI because the project needed a clean JSON API with validation and automatic docs."

## Common Mistakes

- Saying JavaScript and Java are the same. They are different languages.
- Saying FastAPI is the frontend. FastAPI is the backend API framework.
- Saying regex is AI. Regex is rule-based pattern matching.
- Claiming spaCy or transformers are always required. In this project, they are optional or fallback-supported.
- Forgetting to mention Pydantic validation.

## 5 Rapid Fire Questions

1. Why did you use Python?
2. Why FastAPI instead of Flask?
3. What does JavaScript do in the frontend?
4. Why is regex useful in document review?
5. What is the purpose of Pydantic?

## 30 Second Revision Summary

The project uses Python and FastAPI for the backend, Pydantic for validation, HTML/CSS/JavaScript for the frontend dashboard, regex and optional spaCy/transformers for NLP tasks, and Git/GitHub for version control. FastAPI receives document text, Python processes it, and JavaScript renders the JSON result in the browser. The stack is simple, modern, practical, and easy to explain in interviews.
