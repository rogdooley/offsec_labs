# Assignment 04 - Hard Mode SSTI Exploitation

## Goal

Exploit the SSTI vulnerability in the hardened version of the Flask application (`hard_mode_app.py`), despite input character restrictions.

This assignment simulates real-world weak filtering attempts where only certain characters are blocked.

---

## Setup

1. Navigate to the flask_app directory.
2. Run the hardened Flask app:

```bash
python hard_mode_app.py
```
   (Optional: specify a different port if needed.)

3. Access the app at `http://127.0.0.1:5555/` (or your chosen port).

---

## Observations

- Input characters `{}`, `[ ]`, `.`, and `|` are **removed** before rendering the template.
- You cannot use traditional SSTI payloads like `{{7*7}}` directly.
- Creative approaches are required to trigger code execution.

---

## Tasks

1. Confirm that basic payloads are sanitized and fail.
2. Explore alternative injection methods:
   - Can you leverage function calls, filters, or attribute access creatively?
   - Are there alternate expressions that don't rely on `{}` or `.` characters?
3. Achieve template evaluation or code execution despite the filters.
4. Document any successful or failed payloads.

---

## Hints

- Jinja2 allows creative expressions through:
  - String concatenation
  - Using functions like `attr()`
  - Using filters in unexpected ways
- Consider payloads that assemble expressions dynamically rather than writing them outright.

---

## Deliverables

- **Working payloads** that bypass the basic filters (if achieved).
- **Notes on failed attempts** and what you learned.
- **Screenshots** or **copy of server output** showing successful evaluation or code execution.
- **General notes** about strategies you tried.

---

---

## Extra Credit (Optional Challenges)

If you successfully achieve SSTI despite the character restrictions, attempt the following bonus tasks:

1. **Reverse Shell Challenge**
   - Use your payload to open a reverse shell back to your machine.
   - Note: You may need to carefully construct your shell payload using allowed characters.

2. **Environment Discovery**
   - Dump all accessible environment variables from the server.
   - Look for secrets like API keys, database credentials, or tokens.

3. **Command Execution Chain**
   - Chain multiple commands together.
   - Example: Run `id`, `uname -a`, and `whoami` in a single payload.

4. **Alternative Injection Vectors**
   - Identify another input point in the application (besides the `name` field) where injection could occur if the app were expanded.

Document your successes or any challenges you encountered while attempting these extra goals.

---
