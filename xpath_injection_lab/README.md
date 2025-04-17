# XPath Injection Lab

This project contains a deliberately vulnerable web application designed to demonstrate XPath injection vulnerabilities. It serves as the foundation for exploring blind XPath injection techniques through practical exploitation.

## Project Structure

xpath_injection_lab/
├── target_app/
│   ├── app.py                 # Vulnerable Flask app with login logic
│   ├── users.xml              # XML file containing user credentials
│   └── templates/
│       └── login.html         # HTML login form for manual testing
├── attacker_scripts/
│   └── blind_xpath_exploit.py # (Placeholder) Attack script to be developed in Assignment 1
├── requirements.txt           # Python dependencies
└── README.md                  # This file

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

## Disclaimer

This application is intentionally vulnerable and is intended for educational and research purposes only. Do not expose this application to the internet or deploy it in any production environment.
