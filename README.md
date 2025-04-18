# Web Exploitation Labs

A growing collection of offensive security labs and exploit scripts designed for hands-on vulnerability research and skill development. Each lab is self-contained and focuses on a specific vulnerability class or attack technique commonly encountered during web application and infrastructure assessments.

This project reflects a guided, collaborative learning effort. Prompts and assignments were designed through interactive sessions with ChatGPT, while all practical implementation and experimentation was completed manually.


## Project Structure

Each subdirectory represents a focused lab environment, containing:

- A vulnerable target application (usually Flask-based)
- One or more attacker scripts to simulate or automate exploitation
- Supporting files such as sample data, configs, and instructions

---

## Labs

### `xpath_injection_lab/`
Demonstrates how blind XPath injection can be used to extract data from insecure XML-backed login systems.

- `target_app/`: A vulnerable Flask app using unsanitized XPath queries.
- `attacker_scripts/`: Python scripts for blind XPath injection via HTTP.
- Teaches how to abuse logic-based inference with status code side channels.

### Coming Soon
Planned labs include:
- SSTI exploitation in Flask/Jinja2
- CSRF bypasses via DOM-based misconfigurations
- JWT token forgery and none-alg attacks
- Host header injection and cache poisoning
- SSRF via PDF rendering libraries

---

## Goals

- Build practical experience with web exploitation
- Maintain clean, testable Python3 code
- Reinforce red team mindset through automation
- Provide realistic yet controlled attack surfaces

Each lab is built from scratch to reinforce both attacker and defender perspectives.

---

## Attribution

This project is part of an ongoing collaborative lab series developed with the assistance of OpenAI's ChatGPT for educational and offensive security research purposes.

All source code, implementation details, and lab solutions are written and maintained by [Your Name or GitHub Username].

Assignment structure, challenge design, and guidance are the result of an interactive development workflow using ChatGPT as a learning and mentoring assistant.

