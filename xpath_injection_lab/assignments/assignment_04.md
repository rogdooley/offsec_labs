# Assignment 4: Blind Field Name Discovery in XML via XPath Injection

## Objective

Develop a blind inference technique to discover unknown field (element) names within an XML structure during an XPath injection attack. The goal is to infer which child nodes exist under a known parent node (e.g., `<user>`), by probing likely tag names one by one.

This simulates real-world black-box scenarios where the attacker knows high-level objects (like `user`) exist but does not know their internal field layout (e.g., `username`, `password`, `role`).

---

## Requirements

- Build a skeleton Python script that:
  - Guesses field names against a known parent node (`//user`) using XPath injection.
  - Sends crafted payloads targeting different child elements.
  - Uses HTTP status (200 vs 401) to infer existence of a field.
- Attempt discovery of common field names like:
  - `username`, `password`, `role`, `email`, `name`, `account`, `id`, `token`
- Support specifying a custom wordlist of candidate field names

---

## Constraints

- Blind inference only (status code observation)
- No access to the actual XML structure
- One field guess per HTTP request
- Target child elements under `//user`

---

## Sample Probing Strategy

For each candidate field name:

```plaintext
' or substring(//user[1]/candidatefield/text(), 1, 1) = 'a' or '
```

If a 200 response occurs for any character test, infer that the field exists.

---

## Output

Write discovered field names to the specified output file:

```text
Discovered fields:
- username
- password
- role
```

---

## Deliverable

- A skeleton Python script implementing:
  - Argument parsing (`--target`, `--proxy`, `--wordlist`, `--output`)
  - Field probing loop using blind XPath injection
  - Output of discovered fields

This assignment builds toward more advanced real-world exploitation workflows.

