# 07 NLP Concepts For Project

## What Is NLP?

NLP stands for Natural Language Processing. It is a field of artificial intelligence that helps computers work with human language.

Human language includes:

- Sentences
- Paragraphs
- Documents
- Emails
- Contracts
- Reports
- Notes

In this project, NLP is used to analyze business documents and extract useful information from them.

Beginner explanation:

> NLP helps computers read text in a useful way. It does not mean the computer understands language like a human, but it can identify patterns, summarize text, extract key values, and detect important words.

## Why NLP Helps Business Documents

Business documents are usually unstructured. They contain useful information, but it is mixed inside paragraphs.

Example:

```text
The vendor shall pay a penalty if payment is overdue beyond 30 days.
```

A human understands that this sentence contains risk. NLP helps the system identify:

- `penalty` as a risk term
- `overdue` as a payment risk term
- `30 days` as time-related information

NLP makes document review faster by turning raw text into structured output.

## NLP Tasks Used In This Project

This project focuses on practical NLP tasks:

- Text cleaning
- Summarization
- Sentence splitting
- Tokenization conceptually
- Named Entity Recognition
- Regex extraction
- Keyword detection
- Rule-based action generation

It does not use unnecessary research-heavy NLP concepts. The focus is business usefulness.

## Text Cleaning

Text cleaning prepares raw input before analysis.

Raw text can contain:

- Extra spaces
- Line breaks
- Copy-paste formatting
- Empty sections
- Sensitive contact information

The project cleans text by:

- Masking sensitive values like emails and phone numbers.
- Normalizing whitespace.
- Trimming extra spaces.

Why it matters:

- Clean input improves extraction.
- Summaries look better.
- Risk detection becomes more consistent.

## Tokenization

Tokenization means splitting text into smaller units.

Tokens can be:

- Words
- Numbers
- Punctuation
- Subwords

Example:

```text
Payment is overdue.
```

Tokens:

```text
Payment
is
overdue
.
```

### How Tokenization Relates To This Project

The project does not require you to manually tokenize everything, but tokenization is an important NLP concept. Libraries like spaCy and transformer models use tokenization internally.

Risk detection also uses a simple form of text matching by converting text to lowercase and checking whether keywords exist.

Interview answer:

> Tokenization is the process of breaking text into smaller units like words or subwords. It helps NLP systems analyze text. In this project, tokenization is mostly handled internally by NLP libraries, while simpler keyword matching is used for risk detection.

## Sentence Splitting

Sentence splitting means dividing a paragraph into sentences.

Example:

```text
Invoice is overdue. Penalty may apply. Escalation is required.
```

Sentences:

1. Invoice is overdue.
2. Penalty may apply.
3. Escalation is required.

The project uses sentence splitting in fallback summarization. If transformer summarization is unavailable, the system can use the first few sentences as a basic summary.

## Summarization

Summarization means creating a shorter version of a longer text while preserving the main meaning.

### Why Summarization Is Useful

Business users often do not have time to read full documents. A summary helps them quickly understand:

- Topic
- Main issue
- Important obligation
- Overall risk

### Types Of Summarization

There are two common types:

| Type | Meaning | Example |
| --- | --- | --- |
| Extractive | Selects important sentences from original text | First three important sentences |
| Abstractive | Generates a new summary in its own words | LLM or transformer summary |

### Summarization In This Project

The project supports transformer-based summarization when available. It also has a fallback summary that uses the first few sentences.

This is practical because the app remains usable even if heavy AI models are not available.

Interview answer:

> Summarization is used to reduce long business documents into short readable summaries. In my project, the summarizer can use a transformer model if available, but it also has fallback logic so the app remains reliable during demos.

## Named Entity Recognition

Named Entity Recognition, or NER, is the process of identifying important real-world names and values in text.

Common entity types:

- Person
- Organization
- Location
- Date
- Money
- Product

### NER In This Project

The project focuses on business-relevant entities:

- Organizations
- Dates
- Amounts
- Invoice IDs

Example:

```text
Blue Harbour Consulting signed an agreement with Rivergate Foods on 1 April 2026 for $7,500.
```

Extracted entities:

| Entity Type | Value |
| --- | --- |
| Organization | Blue Harbour Consulting |
| Organization | Rivergate Foods |
| Date | 1 April 2026 |
| Amount | $7,500 |

### Why NER Matters

In business documents, the exact details matter. A summary may tell us the document is about a vendor agreement, but entity extraction tells us:

- Which vendor?
- Which date?
- What amount?
- Which invoice?

This turns text into structured business data.

## Keyword Detection

Keyword detection means checking whether specific words appear in text.

In this project, risk keywords include:

- penalty
- overdue
- breach
- liability
- urgent
- escalation
- fraud
- dispute
- non-compliance

### How It Works

The system converts text to lowercase and checks whether each keyword is present.

Example:

```text
The payment is overdue and may attract penalty.
```

Detected:

```text
overdue
penalty
```

### Why Keyword Detection Is Used

Keyword detection is:

- Simple
- Fast
- Explainable
- Easy to improve
- Good for known business risk terms

Interviewers often appreciate simple, clear logic when it is suitable for the problem.

## Rule-Based Systems

A rule-based system uses predefined rules instead of learning everything from data.

Example rule:

```text
If risk flag contains "penalty", add action item "Review penalty clauses."
```

### Why Rule-Based Logic Was Used

Rule-based logic is useful here because:

- Risk terms are known in advance.
- It is easy to explain.
- It does not require a large dataset.
- It is predictable.
- It works well for a first version.

### Limitation

Rule-based systems may miss:

- New wording
- Implied risks
- Negation
- Context

Example:

```text
No penalty will be charged.
```

A simple keyword system may still detect `penalty`.

This is an excellent future improvement point.

## Regex Extraction

Regex means regular expression. It is used to find text patterns.

In this project, regex helps extract:

- Dates
- Amounts
- Invoice IDs
- Organization-like names
- Emails
- Phone numbers
- Bank identifiers

Example regex use case:

```text
INV-20431
```

The invoice pattern can identify this as an invoice ID.

### Why Regex Is Useful For Business Documents

Business documents often contain predictable formats:

- Invoice IDs follow patterns.
- Dates follow patterns.
- Currency values follow patterns.
- Phone numbers follow patterns.

Regex is a good tool for extracting these values quickly.

## Difference Between NLP, Regex, And ML

| Concept | Meaning | Use In Project |
| --- | --- | --- |
| NLP | Broad field of processing language | Overall document analysis |
| Regex | Pattern matching rules | Extract dates, amounts, IDs |
| ML | Models learn from data | Optional summarization, future risk classification |
| Rule-based logic | Human-defined rules | Risk detection and action generation |

## Why This NLP Design Is Practical

The project does not try to overcomplicate the solution. It uses the right level of NLP for a business document review platform:

- Text cleaning for better input.
- Summarization for quick reading.
- Entity extraction for important values.
- Keyword detection for risk visibility.
- Rule-based action generation for practical output.

This makes the project:

- Explainable
- Easy to demo
- Easy to extend
- Suitable for interviews
- Useful for real business workflows

## Strong Interview Answer

> NLP is used in my project to convert unstructured business text into structured insights. The system cleans the text, summarizes it, extracts entities such as organizations, dates, amounts, and invoice IDs, detects business risk keywords, and generates action items. I used a practical combination of rule-based logic, regex, optional spaCy NER, and optional transformer summarization because the goal was to build an explainable and useful business document review system.

## Interview Tip

Do not overclaim. Say the project uses practical NLP techniques for first-pass document review, not perfect legal understanding.

## Common Mistakes

- Saying NLP means only chatbots.
- Confusing tokenization with summarization.
- Saying regex is machine learning.
- Claiming keyword detection understands context perfectly.
- Forgetting to connect NLP concepts to business value.

## 5 Rapid Fire Questions

1. What is NLP?
2. What is summarization?
3. What is Named Entity Recognition?
4. Why is regex useful?
5. What is the limitation of keyword detection?

## 30 Second Revision Summary

NLP helps computers process human language. In this project, NLP is used to clean business text, summarize documents, extract organizations, dates, amounts, and invoice IDs, detect risk keywords, and generate action items. The project uses practical techniques like regex, rule-based logic, optional spaCy, and optional transformer summarization to support business document review.
