# Assignment 1 - Discovering and Exploiting SSTI

## Goal
Find and exploit a Server-Side Template Injection (SSTI) vulnerability in the provided Flask application.

## Instructions

1. **Run the Flask application**:

```bash
cd flask_app
python app.py
```

2. **Interact with the application**:
   - Visit `http://127.0.0.1:5000/`
   - Submit different values into the `name` field.

3. **Test for SSTI**:
   - Submit payloads like:

     ```
     {{7*7}}
     ```

   - Observe if the server processes the template instead of displaying it literally.

4. **Exploit the SSTI**:
   - Try payloads that lead to **code execution**.
   - Example target: run `id` or `whoami` on the server.

5. **Document your results**:
   - Write down:
     - The payloads you used
     - The server’s responses
     - How you achieved code execution (if applicable)
