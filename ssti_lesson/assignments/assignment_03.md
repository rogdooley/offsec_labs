# Assignment 3 - Mitigating SSTI Vulnerabilities

## Goal
Understand how to properly defend against SSTI in Flask applications.

## Instructions

1. **Study safe template rendering**:
   - Use `render_template` instead of `render_template_string`.
   - Escape or sanitize user input.

2. **Fix the app**:
   - Modify `app.py` to use safe rendering.
   - Example:

```python
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    if request.method == 'POST':
        name = request.form.get('name', 'Guest')
    return render_template('index.html', name=name)
```

3. **Create a `templates/index.html`**:

```html
<!doctype html>
<title>Welcome</title>
<h1>Hello, {{ name }}!</h1>
```

4. **Test that SSTI payloads no longer work**.

## Deliverables

- The fixed version of the application.
- A summary explaining why the new version is safe.
