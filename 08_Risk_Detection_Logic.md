# 08 Risk Detection Logic

## Why Risk Detection Exists

Risk detection is one of the most important business features in this project. A summary tells the user what the document is about, but risk detection tells the user what may require attention.

In consulting, audit, finance, compliance, and operations work, certain words often indicate possible business risk. For example:

- `penalty` may indicate financial exposure.
- `overdue` may indicate payment risk.
- `breach` may indicate contract or compliance failure.
- `fraud` may indicate serious investigation risk.
- `escalation` may indicate urgency.

The purpose of the risk detection engine is to scan documents and highlight such terms early.

## What Risk Means In This Project

In this project, risk does not mean the system has proven that something bad happened. It means the document contains language that may require review.

Important distinction:

| Term | Meaning |
| --- | --- |
| Risk flag | A keyword or phrase that may indicate risk |
| Confirmed risk | A human-reviewed issue that has been validated |
| Action item | A recommended next step based on the flag |

Interview answer:

> In my project, risk flags are early warning signals. They do not replace human judgment. They help analysts quickly identify documents or sections that need closer review.

## Risk Keywords Used

The current system detects these business risk terms:

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
- non compliance
- noncompliance

These words were selected because they commonly appear in contracts, invoices, audit notes, compliance memos, and vendor communications.

## Why Each Risk Keyword Matters

| Keyword | Why It Matters |
| --- | --- |
| penalty | May indicate financial charges for missed obligations |
| overdue | Suggests late payment or missed deadline |
| delay | May affect delivery, operations, or contract timelines |
| breach | Indicates possible failure to meet contract or compliance terms |
| terminated | May indicate contract ending or service stoppage |
| termination | Related to contract exit clauses or cancellation risk |
| liability | Points to legal or financial responsibility |
| escalation | Means the issue may require senior attention |
| urgent | Suggests time-sensitive action is required |
| fraud | Indicates serious financial, legal, or compliance concern |
| dispute | Indicates disagreement between parties |
| non-compliance | Indicates failure to meet rules, policies, or regulations |

## How The Keyword Engine Works

The logic is intentionally simple and explainable.

Basic steps:

1. Receive cleaned document text.
2. Convert text to lowercase.
3. Check whether each risk keyword exists in the text.
4. Collect matched keywords.
5. Remove duplicates.
6. Return the risk flag list.

Simplified logic:

```python
lowered = text.lower()
hits = [keyword for keyword in RISK_KEYWORDS if keyword in lowered]
```

Example:

```text
Late payment is overdue and may trigger penalty and escalation.
```

Detected risks:

```text
overdue
penalty
escalation
```

## Why Lowercase Conversion Is Used

Documents may write the same word differently:

- `Penalty`
- `PENALTY`
- `penalty`

By converting text to lowercase, the system can detect the keyword regardless of capitalization.

Example:

```text
The issue requires URGENT escalation.
```

Lowercase:

```text
the issue requires urgent escalation.
```

Detected:

```text
urgent
escalation
```

## Duplicate Removal

If a word appears many times, the system should not show it repeatedly.

Example:

```text
Penalty will apply. Penalty amount is 5%. Penalty notice must be sent.
```

The risk list should show:

```text
penalty
```

not:

```text
penalty, penalty, penalty
```

The project uses a deduplication helper to keep output clean and readable.

## Risk Detection To Action Items

Risk detection becomes more useful when connected to action generation.

The project maps risk flags to recommended actions.

| Risk Flag | Action Item |
| --- | --- |
| overdue | Follow up on overdue payment and confirm the resolution timeline |
| penalty | Review penalty clauses and quantify potential exposure |
| breach | Escalate the breach to compliance and document next steps |
| delay | Confirm delivery timelines and update stakeholders |
| termination/terminated | Validate termination terms and notice requirements |
| liability | Review liability caps and mitigation steps |
| dispute | Capture dispute details and start resolution workflow |
| fraud | Initiate fraud review and preserve supporting evidence |
| non-compliance | Assess compliance gaps and remediation steps |
| urgent/escalation | Assign an owner and set an expedited review deadline |

This makes the output practical. The user does not only see "risk found"; they also see what to do next.

## Business Example: Invoice

Input:

```text
Invoice INV-20431 for $7,500 is overdue. Late payment may result in penalty.
```

Detected risks:

- overdue
- penalty

Recommended actions:

- Follow up on overdue payment and confirm the resolution timeline.
- Review penalty clauses and quantify potential exposure.

Business value:

- Finance team knows this needs payment follow-up.
- Penalty exposure can be reviewed early.

## Business Example: Contract

Input:

```text
Breach of service levels may lead to termination and liability review.
```

Detected risks:

- breach
- termination
- liability

Recommended actions:

- Escalate the breach to compliance and document next steps.
- Validate termination terms and confirm notice requirements.
- Review liability caps and confirm mitigation steps.

Business value:

- Contract risk is visible.
- Legal or compliance team can review the clause.

## Business Example: Compliance Memo

Input:

```text
The audit finding indicates non-compliance and requires urgent escalation.
```

Detected risks:

- non-compliance
- urgent
- escalation

Recommended actions:

- Assess compliance gaps and document remediation steps.
- Assign an owner and set an expedited review deadline.

Business value:

- Audit team can prioritize remediation.
- Issue ownership becomes clearer.

## Why A Rule-Based Engine Is Suitable For Version 1

The current engine is rule-based. That means it uses predefined keywords and action mappings.

This is suitable for version 1 because:

- It is easy to understand.
- It is fast to run.
- It does not require training data.
- It produces explainable results.
- It is easy to customize for a company.

For an internship project, explainability is a strength. Interviewers can understand exactly how risks are detected.

## Limitations Of Keyword-Based Risk Detection

The keyword approach has limitations.

### 1. No Deep Context Understanding

Example:

```text
No penalty will be charged.
```

The system may detect `penalty`, even though the sentence says there is no penalty.

### 2. Synonym Gaps

The system may miss words not in the list.

Example:

- "default"
- "violation"
- "late fee"
- "chargeback"

If these are not in the keyword list, they may not be detected.

### 3. False Positives

A false positive means the system flags something that is not actually risky.

Example:

```text
Penalty policy was removed from the agreement.
```

The word exists, but the risk may be reduced.

### 4. False Negatives

A false negative means the system misses a real issue.

Example:

```text
The vendor failed to meet agreed service levels.
```

This may imply breach, but the exact word `breach` is not present.

## Future ML Improvements

The risk engine can be improved using machine learning and more advanced NLP.

Possible upgrades:

- Add more risk keywords and synonyms.
- Use phrase matching instead of simple keyword matching.
- Use negation detection for phrases like "no penalty."
- Use sentence-level risk classification.
- Train a model on labeled business documents.
- Use LLMs to classify risk severity.
- Add risk categories such as financial, legal, compliance, operational.
- Add severity levels such as low, medium, high.
- Highlight the sentence where the risk was found.

## Future Risk Severity Scoring

A future version could calculate severity.

Example:

| Risk Term | Severity |
| --- | --- |
| fraud | High |
| breach | High |
| liability | High |
| penalty | Medium |
| overdue | Medium |
| delay | Medium |
| urgent | Context-dependent |

This would help users prioritize documents.

## How To Explain This In Interview

Strong answer:

> The risk detection engine is currently rule-based. It converts the document text to lowercase and checks for predefined business risk keywords such as penalty, overdue, breach, liability, fraud, dispute, and non-compliance. When risks are detected, the system maps them to recommended action items. I chose this approach for version 1 because it is fast, explainable, and does not require a labeled dataset. I also understand its limitations, such as false positives and lack of context, so future improvements would include sentence-level classification, negation handling, and ML-based risk scoring.

## Interview Tip

Always mention that risk flags are indicators, not final decisions. This shows maturity and avoids overclaiming.

## Common Mistakes

- Saying keyword detection is the same as deep AI understanding.
- Ignoring false positives and false negatives.
- Forgetting to connect risk flags with action items.
- Saying the system gives legal advice. It does not.
- Not explaining why rule-based logic is acceptable for version 1.

## 5 Rapid Fire Questions

1. How does the system detect risk terms?
2. Why is lowercase conversion used?
3. What is a false positive?
4. Why is `fraud` a serious risk keyword?
5. How can risk detection be improved in the future?

## 30 Second Revision Summary

The risk detection engine scans cleaned document text for predefined business risk keywords such as penalty, overdue, breach, liability, urgent, fraud, dispute, and non-compliance. It returns unique risk flags and maps them to practical action items. The approach is rule-based, fast, and explainable, but it has limitations such as false positives, missing synonyms, and weak context understanding. Future upgrades can add ML classification, severity scoring, and negation handling.
