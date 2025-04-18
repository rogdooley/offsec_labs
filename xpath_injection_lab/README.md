# XPath Injection Lab

This project contains a deliberately vulnerable web application designed to demonstrate XPath injection vulnerabilities. It serves as the foundation for exploring blind XPath injection techniques through practical exploitation.

## Current Status

The following components have been implemented:

- A vulnerable Flask web application with a `/login` route
- Insecure XPath query logic that uses unsanitized user input
- A basic HTML login form served at the root route
- A sample users.xml file containing two hardcoded users
- Session-based login tracking using Flask’s built-in session handling
- Proper HTTP status differentiation between successful and failed logins (200 vs 401), making it suitable for blind XPath injection attacks

## How to Run the Application

1. Navigate to the target_app directory:
   `cd target_app`

2. Install the required dependencies:
   `pip install -r ../requirements.txt`

3. Start the server on port 5000:
   `python3 app.py --port 5000`

4. Visit the app in your browser at:
   http://127.0.0.1:5000/

## XML User Data

The users.xml file contains sample user accounts:


## Next Steps

The next phase of this lab will involve creating an attacker script to perform blind XPath injection. The script will iteratively brute-force valid usernames using crafted payloads and inference based on HTTP response codes.

## Requirements

- Flask
- lxml

Dependencies can be installed using:

`pip install -r requirements.txt`
# XPath Injection Lab

This lab contains a deliberately vulnerable web application designed to demonstrate XPath injection vulnerabilities. It serves as the foundation for a guided series of assignments focused on blind XPath injection and XML-based authentication bypass techniques.

## Lab Overview

This lab simulates a login portal that uses an XML backend for user authentication and performs XPath queries using unsanitized input. It is used in multiple assignments within the `web-exploitation-labs` project to explore real-world exploitation strategies in a controlled environment.

---

## Current Features

- A Flask-based web application vulnerable to XPath injection
- HTML login form served at the root (`/`)
- Insecure XPath logic using `lxml.etree` and string interpolation
- Sample `users.xml` file containing multiple users with roles (user/admin)
- Session tracking via Flask's built-in session object
- Login endpoint (`/login`) that returns:
  - `200 OK` on success
  - `401 Unauthorized` on failure — usable for blind inference
- Logging of incoming XPath queries for debugging purposes
- Configurable server port and optional SSL support

---

## How to Run

1. Navigate to the target application:
   ```bash
   cd xpath_injection_lab/target_app
   ```

2. Install dependencies:
   ```bash
   pip install -r ../../requirements.txt
   ```

3. Run the vulnerable app:
   ```bash
   python3 app.py --port 5000
   ```

4. Open the login page in your browser:
   ```
   http://127.0.0.1:5000/
   ```

---

## Included Sample Data

The `users.xml` file contains sample credentials for 20+ users with mixed roles, such as:

```xml
<user>
  <username>charlie</username>
  <password>Ch@c0L8Riv3r</password>
  <role>admin</role>
</user>
```

These are used in Assignments 0–3 to test blind XPath extraction of:
- Admin usernames
- Admin passwords
- All usernames and roles

---

## Assignments Covered

This lab supports the following assignments:

- **Assignment 0**: Implement the vulnerable login application
- **Assignment 1**: Blind XPath extraction of admin usernames
- **Assignment 2**: Inference-based extraction of admin passwords
- **Assignment 3**: Full user and role enumeration using XPath

All assignments are written in Markdown and reside in the top-level project directory.

---

## Requirements

- Python 3.x
- Flask
- lxml

Install with:
```bash
pip install -r requirements.txt
```

---

## Security Notice

This application is **intentionally vulnerable** and is for research and educational use only.

**Do not expose this lab to public networks or deploy it in production.**

## Disclaimer

This application is intentionally vulnerable and is intended for educational and research purposes only. Do not expose this application to the internet or deploy it in any production environment.
