# Assignment 2: Blind XPath Extraction of Admin Passwords

## Objective

Expand the existing blind XPath injection tool to extract the **passwords** of users with `role='admin'`, using the same inference-based technique. The server returns HTTP 200 on a correct guess, and 401 otherwise. You will use XPath functions to retrieve one character at a time from each admin user's password field.

---

## Requirements

- Build upon your existing `blind_xpath_exploit.py` infrastructure
- For each `admin` user (indexed as `[1]`, `[2]`, etc.):
  - Use `substring()` to extract each character of the password
  - Use HTTP response status as a boolean oracle
- Stop when no character at the current index returns 200
- Only add a password to the final results if at least one character was successfully extracted

---

## Constraints

- Use only `substring(...) = 'x'` for matching
- Search characters using the same character set as Assignment 1
- Password length is unknown; loop until no match found for a position
- Do not reuse extracted usernames from Assignment 1 — rediscover admins as needed

> Optional variation: you may use the usernames discovered in Assignment 1 to extract corresponding passwords by first identifying the user index associated with a given admin username. This would demonstrate mapping between identity and credentials.

---

## Sample XPath Query Structure

```xpath
substring(//user[role='admin'][1]/password/text(), 5, 1) = 's'
```

This query returns true if the 5th character of the first admin user's password is `s`.

Inject this via the vulnerable `username` field, preserving the structure:

```plaintext
' or substring(//user[role='admin'][1]/password/text(), 5, 1) = 's' or '
```

---

## Output

- Write the discovered passwords to the output file along with their admin index:

```
admin[1] password: S3cr3tP@ss
admin[2] password: R00t4dm1n
```

- Use the same `--output` argument to define the output file path
- Continue supporting `--proxy`, `--delay`, and `--verbose`

---

## Deliverable

Update your existing tool or write a new function in the same script to extract admin passwords.

You may reuse helper functions and logging structure.

Submit the updated script and a short summary of changes when complete.

