# Assignment 01: Exploit via Hash Fragment Injection

## Objective

Demonstrate how an attacker can exploit a CSRF vulnerability by injecting a CSRF token into the DOM using the `location.hash` fragment and smuggling it into an authenticated request.

## Steps

1. Start the vulnerable Flask app in `target_app/`.
2. Open the attack page `attacker_scripts/iframe_exploit.html` in your browser.
3. Confirm that the victim's email has changed to `attacker@evil.com`.
4. Explain why this attack works in a few sentences.

## Questions

- Why is reading the token from `location.hash` insecure?
- What browser feature(s) allow this attack to succeed?
- Would SameSite cookie protections stop this exploit?
