# Assignment Index

This document tracks all assignments completed as part of the `xpath_injection_lab` project under the `offsec_labs` repository. Each assignment builds on the previous one, guiding the development of a vulnerable web application and accompanying exploit scripts.

## XPath Injection Lab

### Assignment 0: Vulnerable XPath-Based Login App
- Description: Build a Flask app that performs unsafe XPath authentication using data from an XML file.
- Focus: Web application setup, session handling, unsafe XPath usage
- Status: Complete
- [View Assignment 0](assignment_00.md)

### Assignment 1: Blind XPath Injection to Extract Admin Usernames
- Description: Write a Python script that uses blind XPath injection to extract usernames of users with the role `admin`.
- Focus: Inference-based exploitation, XPath manipulation, automation
- Status: In Progress
- [View Assignment 1](assignment_01.md)

### Assignment 2: Blind XPath Extraction of Admin Passwords
Extend the existing tool to extract the passwords of admin users using blind XPath injection. The script should infer each password one character at a time by testing `substring()` conditions and observing HTTP 200/401 responses. Optionally, use previously discovered usernames to map credentials directly.
[View Assignment 2](assignment_02.md)


---

## Coming Soon

Future assignments will expand into:

- Password exfiltration via XPath injection
- Privilege escalation by exploiting insecure role checks
- Login bypass using XPath short-circuit logic
- Automation and reporting improvements for the exploit script
- Converting the lab into a CTF-style challenge

---

Each assignment is standalone and can be reused or adapted for other web exploitation labs.

