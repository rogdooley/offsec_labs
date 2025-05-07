# Assignment 03: Use postMessage to Inject Token

## Objective

Simulate a more advanced attacker using `window.postMessage` to inject a forged CSRF token into a victim window or iframe.

## Steps

1. Set up a modified `iframe_exploit.html` that uses `postMessage`.
2. In the target app, add a message listener in JavaScript that reads the CSRF token from `event.data`.
3. Trigger a successful CSRF by sending a message with the token `securetoken123`.

## Questions

- How does using `postMessage` expand the attack surface?
- What origin checks should you implement before trusting message data?
