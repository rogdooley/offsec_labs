# Assignment 3: Inference-Based User Enumeration via XPath Injection

## Objective

Extend the XPath injection tool to extract **all users**, regardless of role, and output both usernames and their associated roles. The goal is to enumerate the full contents of the XML user database by inferring user attributes one character at a time.

This task simulates reconnaissance against systems where XPath injection is possible, but filtering by role is not yet enforced or necessary.

---

## Requirements

- Modify your existing tool to:
  - Enumerate users from index `[1]` to `[N]`
  - Extract each user's `username` and `role` fields
- Use `substring()` for character-by-character inference
- Use HTTP status code as the response oracle
- Loop ends when a user at a given index returns no match

---

## Constraints

- Use XPath queries in the format:
  ```xpath
  substring(//user[{index}]/username/text(), {pos}, 1) = 'c'
  substring(//user[{index}]/role/text(), {pos}, 1) = 'a'
  ```
- Extract only usernames and roles — no password discovery in this assignment
- Match exact values, one character at a time (no `contains()` or regex)

---

## Output

Write the results to your output file in the following format:

```text
user[1] username: alice, role: user
user[2] username: bob, role: user
user[3] username: charlie, role: admin
```

Use `--output` to control the filename.

---

## Optional Enhancements

- Support a new `--extract all` option to trigger full enumeration
- Add a `--max-users` argument to limit the scan range
- Implement a dry-run mode for query preview without sending requests

---

## Deliverable

Add support for full user enumeration and role extraction in your blind XPath injection tool. The new functionality can be included as a new `--extract all` option or integrated into your main script with a dedicated function.

Update your script and output a `.txt` file with discovered user/role pairs. Submit the updated code and a brief summary of what changed.

