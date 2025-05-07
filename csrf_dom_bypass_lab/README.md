# CSRF via DOM-Based Misconfiguration

This lab demonstrates how CSRF protections can be bypassed when a web application reads CSRF tokens from untrusted sources like `location.hash` or query parameters.

## Scenario

The vulnerable app uses a CSRF token (`securetoken123`) for email change requests. The client-side JavaScript reads this token from the URL hash, which can be injected by an attacker using a crafted iframe.

## Run the Lab

1. Start the app:
    ```bash
    FLASK_APP=app.py flask run
    ```

2. Open the attacker's exploit page in a browser:
    ```bash
    firefox attacker_scripts/iframe_exploit.html
    ```

3. Observe that the victim's email was changed without interaction.

## Learning Points

- Do not read CSRF tokens from attacker-controllable DOM sources.
- Always validate CSRF tokens server-side.
- Avoid reading tokens from `location.hash`, query strings, or localStorage unless explicitly secured.
