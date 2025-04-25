# Bonus Challenge - No Braces Allowed

## Goal

Exploit the SSTI vulnerability in the Flask app **without using curly braces `{}`**. This simulates environments with naive input sanitization that blocks obvious patterns.

## Instructions

1. Run the vulnerable Flask app.
2. Attempt payloads that bypass `{}` restrictions.
3. Get the application to:
   - Render input dynamically, or
   - Execute unintended logic (bonus: achieve code execution)
4. Techniques to explore:
   - Using `+`, `*`, or function calls instead of expression blocks
   - Leveraging control structures or function filters (e.g., `name|attr('upper')`)
   - Using raw expressions in default filters

## Deliverables

- Payloads that demonstrate successful SSTI without `{}`.
- Description of how each payload worked.
- Server response screenshots or summaries.

**Hint**: Jinja2 allows lots of creative logic — even in filters.

---
