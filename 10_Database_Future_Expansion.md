# 10 Database Future Expansion

## Current Database Status

The current version of the AI-Powered Document Review & Risk Insights Platform does not require a database for its core demo.

Current behavior:

1. User submits text or uploads a `.txt` file.
2. Backend analyzes it immediately.
3. Backend returns the result.
4. Frontend displays it.
5. The report is not permanently saved.

This is acceptable for a first version because the main goal is to demonstrate document analysis, API design, and dashboard output.

## Why Add A Database Later?

A database would make the platform more realistic for business use.

Without a database:

- Reports disappear after the page is refreshed.
- Users cannot view history.
- There is no long-term analytics.
- Multiple users cannot manage saved documents.

With a database:

- Users can save reports.
- Teams can search previous analyses.
- Managers can track risk trends.
- Audit logs can be maintained.
- User accounts can be supported.

## What Data Could Be Stored?

The platform could store:

- User accounts
- Uploaded document metadata
- Analysis reports
- Extracted entities
- Risk flags
- Action items
- Confidence scores
- Processing logs
- User feedback
- Audit trail events

## MongoDB Option

MongoDB is a NoSQL document database. It stores data in JSON-like documents.

### Why MongoDB Fits This Project

The project output is already JSON-like:

```json
{
  "summary": "...",
  "key_entities": {...},
  "risk_flags": [...],
  "action_items": [...]
}
```

MongoDB can store this kind of structure naturally.

### MongoDB Benefits

- Flexible schema.
- Good for JSON-like reports.
- Easy to store nested data.
- Useful when fields may evolve.
- Good for rapid prototyping.

### Example MongoDB Report Document

```json
{
  "_id": "report_001",
  "user_id": "user_123",
  "document_name": "vendor_agreement.txt",
  "document_type": "contract",
  "created_at": "2026-04-29T10:30:00Z",
  "summary": "Vendor agreement includes payment and penalty terms.",
  "key_entities": {
    "organizations": ["Blue Harbour Consulting", "Rivergate Foods"],
    "dates": ["1 April 2026"],
    "amounts": ["$7,500"],
    "invoice_ids": ["INV-20431"]
  },
  "risk_flags": ["penalty", "escalation"],
  "action_items": ["Review penalty clauses."],
  "confidence_score": "High"
}
```

## MySQL Option

MySQL is a relational database. It stores data in tables with rows and columns.

### Why MySQL Could Fit

MySQL is useful if the platform needs:

- Strong structured relationships.
- User accounts.
- Organization/team tables.
- Report history.
- Analytics queries.

### MySQL Benefits

- Mature and reliable.
- Strong query language.
- Good for structured business data.
- Works well for reporting.
- Common in enterprise systems.

## Example MySQL Schema

### Users Table

| Column | Type | Purpose |
| --- | --- | --- |
| `id` | INT/UUID | Unique user ID |
| `name` | VARCHAR | User name |
| `email` | VARCHAR | Login email |
| `role` | VARCHAR | Analyst, manager, admin |
| `created_at` | DATETIME | Account creation time |

### Documents Table

| Column | Type | Purpose |
| --- | --- | --- |
| `id` | INT/UUID | Unique document ID |
| `user_id` | INT/UUID | Owner/uploader |
| `file_name` | VARCHAR | Uploaded file name |
| `document_type` | VARCHAR | Contract, invoice, memo |
| `created_at` | DATETIME | Upload time |

### Reports Table

| Column | Type | Purpose |
| --- | --- | --- |
| `id` | INT/UUID | Unique report ID |
| `document_id` | INT/UUID | Related document |
| `summary` | TEXT | Document summary |
| `confidence_score` | VARCHAR | High, Medium, Low |
| `created_at` | DATETIME | Analysis time |

### Risks Table

| Column | Type | Purpose |
| --- | --- | --- |
| `id` | INT/UUID | Unique risk row |
| `report_id` | INT/UUID | Related report |
| `risk_term` | VARCHAR | penalty, overdue, fraud |
| `severity` | VARCHAR | Future field: Low/Medium/High |

### Action Items Table

| Column | Type | Purpose |
| --- | --- | --- |
| `id` | INT/UUID | Unique action row |
| `report_id` | INT/UUID | Related report |
| `action_text` | TEXT | Recommended action |
| `status` | VARCHAR | Pending, In Progress, Done |
| `owner_id` | INT/UUID | Assigned user |

## MongoDB vs MySQL For This Project

| Requirement | Better Fit |
| --- | --- |
| Store flexible JSON reports | MongoDB |
| Store structured users and roles | MySQL |
| Rapid prototype | MongoDB |
| Complex relational reporting | MySQL |
| Enterprise finance-style schema | MySQL |
| Evolving NLP output fields | MongoDB |

Strong answer:

> If the focus is flexible document reports, MongoDB is a natural fit because the analysis output is JSON-like. If the platform needs strict user management, reporting, and relational analytics, MySQL is a strong option.

## User Accounts

Adding a database would enable user accounts.

User account features:

- Sign up
- Login
- Saved reports
- Role-based permissions
- Team access
- User-specific history

Example roles:

- Analyst: upload and review documents.
- Manager: view team reports.
- Admin: manage users and settings.

## Saved Reports

Saved reports would allow users to revisit previous analyses.

Useful report fields:

- Report ID
- Document name
- Upload date
- Summary
- Risk count
- Confidence score
- Status
- Assigned owner

This makes the app closer to a real enterprise dashboard.

## History

History helps users answer:

- Which documents were reviewed this week?
- Which had high-risk terms?
- Which invoices were overdue?
- Which action items are still pending?

History is important for audit and compliance workflows because teams often need evidence of review.

## Analytics

A database enables analytics dashboards.

Possible analytics:

- Number of documents reviewed.
- Most common risk flags.
- High-risk document percentage.
- Average confidence score.
- Pending action items.
- Risk trends by month.
- Risk count by vendor.

Example:

```text
Top risk keywords this month:
1. overdue
2. penalty
3. dispute
```

## Logs

Logs store events and system behavior.

Useful log events:

- User uploaded document.
- Analysis started.
- Analysis completed.
- API error occurred.
- Report viewed.
- Action item updated.

Logs are useful for:

- Debugging
- Compliance
- Auditing
- Security monitoring

## Data Privacy Considerations

If a database is added, privacy becomes more important.

Consider:

- Do not store sensitive data unnecessarily.
- Mask emails, phone numbers, and bank information.
- Encrypt sensitive fields.
- Use access controls.
- Add retention policies.
- Allow deletion of old reports.

Business documents can contain confidential information, so database design must be careful.

## Future API Endpoints With Database

Possible future endpoints:

| Endpoint | Method | Purpose |
| --- | --- | --- |
| `/reports` | GET | List saved reports |
| `/reports/{id}` | GET | View one report |
| `/reports/{id}` | DELETE | Delete report |
| `/users/login` | POST | Authenticate user |
| `/actions/{id}` | PATCH | Update action status |
| `/analytics/risks` | GET | View risk trends |

## Strong Interview Answer

> The current version does not use a database because it focuses on real-time document analysis. A database would be the next step to support user accounts, saved reports, report history, analytics, logs, and action tracking. MongoDB would fit well for storing flexible JSON-like analysis results, while MySQL would fit well for structured user accounts, reports, risks, and action item tables.

## Interview Tip

If asked why you did not use a database, do not sound defensive. Say the first version focuses on core NLP and API flow, and database support is a clear future expansion.

## Common Mistakes

- Saying every project must have a database.
- Choosing MongoDB or MySQL without explaining why.
- Forgetting privacy concerns.
- Not thinking about report history.
- Storing raw confidential documents without access controls.

## 5 Rapid Fire Questions

1. Does the current project use a database?
2. Why would a database be useful later?
3. Why might MongoDB fit this project?
4. Why might MySQL fit this project?
5. What data should be stored for saved reports?

## 30 Second Revision Summary

The current project analyzes documents in real time and does not need a database for the core demo. A future database could store users, documents, reports, risks, action items, history, analytics, and logs. MongoDB is suitable for flexible JSON-like reports, while MySQL is suitable for structured relational data such as users, reports, and action tracking.
