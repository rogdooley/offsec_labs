# Assignment 04: Implement Proper CSRF Token Handling

## Objective

Harden the application against all forms of DOM-based CSRF bypasses using secure server-validated tokens and strict SameSite policies.

## Steps

1. Generate the CSRF token on the server.
2. Store it in a secure, `HttpOnly`, SameSite cookie.
3. Remove all client-side logic that attempts to read or set the token.
4. Ensure token validation works regardless of attacker-controlled DOM.

## Questions

- Why is server-side token generation and validation more secure?
- Can SameSite cookies alone prevent CSRF?
- What lessons can you apply to real-world single-page apps?
