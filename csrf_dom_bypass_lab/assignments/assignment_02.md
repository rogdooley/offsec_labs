# Assignment 02: Modify the Token Validation Mechanism

## Objective

Alter the Flask server to generate a unique CSRF token per session and store it in a secure cookie. Then observe how the original DOM-based logic fails.

## Steps

1. Modify `app.py` to issue a CSRF token in a `Set-Cookie` header.
2. Store the token server-side (in memory is fine).
3. Update the fetch handler in `change_email.js` to try and read it from the DOM.
4. Note what happens when the exploit page is loaded.

## Questions

- What breaks in the exploit when the token is no longer in the DOM?
- What would a secure client-side implementation look like?
