# 06 Frontend Deep Dive

## What The Frontend Does

The frontend is the user-facing part of the AI-Powered Document Review & Risk Insights Platform. It allows users to submit business documents and view structured analysis results.

The frontend is built with:

- HTML for structure.
- CSS for design.
- JavaScript for interactivity and API communication.

The main frontend files are:

| File | Purpose |
| --- | --- |
| `frontend/index.html` | Defines page structure and UI elements |
| `frontend/styles.css` | Controls layout, colors, cards, responsiveness, and animations |
| `frontend/app.js` | Handles tabs, input, API calls, loading states, errors, and result rendering |

## Frontend User Flow

From the user's perspective:

1. Open the dashboard.
2. Choose "Paste Text" or "Upload File."
3. Enter business document text or select a `.txt` file.
4. Click "Analyze Document."
5. Wait while the request is processed.
6. View the summary, key entities, risk flags, action items, and confidence score.

Simple flow:

```text
User input
    |
    v
JavaScript reads input
    |
    v
fetch API call to backend
    |
    v
Backend returns JSON
    |
    v
JavaScript updates DOM
    |
    v
User sees dashboard cards
```

## `index.html` Structure

`index.html` defines the page skeleton.

Major sections:

- `<head>` for metadata, title, fonts, and CSS link.
- `<header>` for brand and short product positioning.
- `<main>` for the primary dashboard.
- Input card for text/file submission.
- Results area for analysis output.
- `<script src="app.js">` for JavaScript.

## Header And Branding

The header contains:

- Brand mark: `AI`
- Project name
- Subtitle: Business Document Intelligence System
- Short note about consulting, audit, finance, and compliance teams

This makes the project feel professional and business-oriented.

Interview note:

> I designed the UI as a business dashboard rather than a casual text demo because the target users are professional teams reviewing documents.

## Input Card

The input card is the area where users provide the document.

It contains:

- Card header
- Two tabs: Paste Text and Upload File
- Textarea
- File picker
- Sample text button
- Analyze button
- Error box
- Status message

## Textarea

The textarea allows users to paste business text.

Example placeholder content:

```text
ABC Technologies entered a 12 month vendor agreement with Sigma Logistics...
```

Why textarea is useful:

- Allows long text input.
- Easy to test during demos.
- Avoids needing file upload for every example.

## Upload UI

The upload UI allows users to select a `.txt` document.

Important elements:

- A label styled as a file input.
- Hidden actual file input.
- File name display.
- Hint saying supported format is plain text.

The actual input is hidden for better design, while the label acts as the visible upload control.

## Tabs

The UI has two tabs:

- Paste Text
- Upload File

JavaScript switches the active tab. When the user changes tabs, the app clears old input and resets status messages.

Why tabs help:

- They avoid clutter.
- They separate two input modes.
- They make the interface easy to understand.

## Analyze Button

The Analyze button triggers the API call.

In JavaScript, an event listener handles the click:

```javascript
analyzeBtn.addEventListener("click", async () => {
  // validate input
  // send request
  // render result
});
```

The button also supports a loading state. While analysis is running:

- The button is disabled.
- A spinner appears.
- Status text changes.

This prevents duplicate requests and gives feedback to the user.

## Results Cards

The results area contains cards for:

- Summary
- Key Entities
- Risk Flags
- Action Items
- Confidence Score

### Summary Card

Displays the short summary returned by the backend.

### Key Entities Card

Displays:

- Organizations
- Dates
- Amounts
- Invoice IDs

The entities are shown as chips, which are small badge-like labels.

### Risk Flags Card

Displays detected risk keywords as a list.

Examples:

- penalty
- overdue
- breach
- liability

### Action Items Card

Displays recommended next steps.

Example:

```text
Review penalty clauses and quantify potential exposure.
```

### Confidence Score Card

Displays a badge such as:

- High
- Medium
- Low

This gives users a quick idea of how complete the extraction appears.

## `app.js` Logic

`app.js` is responsible for browser behavior.

It does several important jobs:

- Selects DOM elements.
- Stores API base URL.
- Manages tabs.
- Inserts sample text.
- Handles file selection.
- Sends requests to backend.
- Handles loading state.
- Handles errors.
- Renders results.
- Escapes HTML for safety.

## DOM Element Selection

At the top of `app.js`, JavaScript selects elements by ID:

```javascript
const documentText = document.getElementById("documentText");
const analyzeBtn = document.getElementById("analyzeBtn");
const summaryOutput = document.getElementById("summaryOutput");
```

This lets JavaScript read input values and update output areas.

## API Base URL

The frontend uses:

```javascript
const API_BASE = "http://127.0.0.1:8000";
```

This tells JavaScript where the FastAPI backend is running.

In production, this would be changed to the deployed backend URL.

## Fetch API

The Fetch API is used to send HTTP requests from JavaScript.

### Text Analysis Request

For pasted text:

```javascript
const response = await fetch(`${API_BASE}/analyze-text`, {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
  },
  body: JSON.stringify({ text }),
});
```

Explanation:

- `method: "POST"` sends data for processing.
- `Content-Type: application/json` tells backend the body is JSON.
- `JSON.stringify({ text })` converts JavaScript object to JSON string.

### File Upload Request

For uploaded files:

```javascript
const formData = new FormData();
formData.append("file", file);

const response = await fetch(`${API_BASE}/upload-document`, {
  method: "POST",
  body: formData,
});
```

No manual `Content-Type` is set for `FormData` because the browser automatically sets the correct multipart boundary.

## Error Handling In Frontend

The frontend checks:

- If no file is selected.
- If pasted text is empty.
- If backend returns an error response.
- If the network request fails.

The error message is displayed in the error box.

Example:

```text
Analysis failed: Text input cannot be empty
```

Good error handling improves user experience and makes the app easier to demo.

## Loading State

The function `setLoading(isLoading)` disables the button and toggles a loading class.

Why it matters:

- Prevents duplicate clicks.
- Shows that processing is happening.
- Makes the app feel responsive.

## Rendering Results

The `renderResults(data)` function updates the UI using backend JSON.

It updates:

- `summaryOutput`
- `orgList`
- `dateList`
- `amountList`
- `invoiceList`
- `riskList`
- `actionList`
- `confidenceScore`

This is where the API response becomes visible to the user.

## Rendering Chips

Entities are displayed as chips.

If no item is found, the UI shows:

```text
None detected
```

This is better than leaving the area empty because the user knows the system completed the check.

## Rendering Lists

Risk flags and action items are rendered as list items.

If no items are found:

```text
None detected.
```

## HTML Escaping

The frontend uses an `escapeHtml` function before inserting values into `innerHTML`.

Why this matters:

- User-provided text may contain HTML-like characters.
- Escaping reduces the risk of unwanted HTML injection.
- It is a basic frontend safety practice.

Interview answer:

> I used HTML escaping when rendering dynamic chips and list items so that user-provided text is displayed as text rather than interpreted as HTML.

## CSS Styling

`styles.css` controls visual design.

Important styling areas:

- Root color variables.
- Body background.
- Sticky navbar.
- Dashboard shell width.
- Hero section.
- Input card.
- Result cards.
- Tabs.
- Buttons.
- File input.
- Chips.
- Lists.
- Confidence badge.
- Error and status messages.
- Responsive layout.

## Responsive Design

Responsive design means the UI adapts to different screen sizes.

The CSS uses media queries:

- On large screens, input and results can appear side by side.
- On smaller screens, the layout becomes a single column.
- The navbar adapts on mobile.

Why this matters:

- The project looks better during demos.
- Users can access it from laptops or smaller screens.
- It shows frontend awareness beyond basic HTML.

## How Frontend Talks To Backend

Complete communication flow:

```text
User clicks Analyze
        |
        v
app.js validates input
        |
        v
app.js sends fetch request
        |
        v
FastAPI receives request
        |
        v
Backend processes document
        |
        v
Backend returns JSON
        |
        v
app.js parses response.json()
        |
        v
renderResults updates dashboard
```

## Why Plain JavaScript Was Enough

The project does not require a large frontend framework because it has one main screen and limited interactions.

Plain JavaScript is enough for:

- Form handling
- Tab switching
- API calls
- DOM updates
- Error messages

React or Vue could be added later if the app grows into:

- Multi-page dashboard
- User accounts
- Saved reports
- Complex state management
- Reusable component library

## Strong Interview Answer

> The frontend is built with HTML, CSS, and JavaScript. `index.html` defines the dashboard structure, including the input card, tabs, textarea, file upload, and result cards. `styles.css` creates a responsive business dashboard design. `app.js` manages user interactions, sends `fetch` requests to the FastAPI backend, handles loading and errors, parses the JSON response, and updates the DOM with summary, entities, risks, actions, and confidence score.

## Interview Tip

When explaining frontend, do not just say "I made a UI." Explain the user flow and how the UI communicates with the backend.

## Common Mistakes

- Saying HTML sends the API request. JavaScript sends the request.
- Forgetting to mention `fetch`.
- Not knowing why `FormData` is used for file uploads.
- Ignoring loading and error states.
- Saying CSS is only for colors. CSS also handles layout and responsiveness.

## 5 Rapid Fire Questions

1. What does `index.html` contain?
2. What does `app.js` do?
3. What is the Fetch API?
4. Why is `FormData` used?
5. How are backend results shown to the user?

## 30 Second Revision Summary

The frontend uses HTML for structure, CSS for a responsive business dashboard, and JavaScript for interactivity. Users paste text or upload a `.txt` file, then JavaScript sends a POST request to FastAPI using `fetch`. The backend returns JSON, and JavaScript renders summary, entities, risk flags, action items, and confidence score into UI cards.
