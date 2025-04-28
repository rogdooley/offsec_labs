# Assignment 05 - Multi-Vector SSTI Exploitation

## Goal

Identify and exploit Server-Side Template Injection vulnerabilities across multiple inputs in the hardened multi-vector Flask app (`multi_vector_hard_mode_app.py`).

---

## Setup

1. Navigate to the flask_app directory.
2. Run the multi-vector hard mode app:

```bash
python multi_vector_hard_mode_app.py
```
   (Optional: specify a different port if needed.)

3. Access the app at `http://127.0.0.1:5555/` (or your chosen port).

---

## Observations

- The application accepts input from:
  - POST fields: `name`, `email`, `comments`
  - GET parameter: `greeting`
  - HTTP header: `X-User-Info`
- Only the `name` field applies character filtering for `{}`, `[ ]`, `.`, and `|`.
- Other fields are injected into the template **without filtering**.

---

## Tasks

1. Test each input individually for SSTI vulnerabilities.
2. Determine which inputs are exploitable.
3. Attempt to bypass the filtering on the `name` field.
4. Successfully achieve template evaluation or code execution through at least one input.
5. Document which inputs were vulnerable and how you exploited them.

---

## Hints

- Some inputs will be easier to exploit than others.
- Consider using different payloads depending on input context (GET, POST, Headers).
- Think about injecting payloads that do not require `{}` if necessary.

---

## Deliverables

- List of vulnerable input points.
- Working payloads for each vulnerable input.
- Screenshots or output proof of successful template evaluation or command execution.
- Notes on failed attempts and observations.

---
