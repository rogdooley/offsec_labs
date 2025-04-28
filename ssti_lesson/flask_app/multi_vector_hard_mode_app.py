from flask import Flask, request, render_template_string
import sys

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    name = ''
    email = ''
    comments = ''
    greeting = request.args.get('greeting', 'Hello')
    user_info = request.headers.get('X-User-Info', 'No Info Provided')

    if request.method == 'POST':
        name = request.form.get('name', 'Guest')
        email = request.form.get('email', 'noemail@example.com')
        comments = request.form.get('comments', '')

        # Apply basic filtering only to 'name' field
        forbidden = "{}[].|"
        for char in forbidden:
            name = name.replace(char, '')

    template = (
        "<html>"
        "<head><title>Multi-Vector SSTI Challenge</title></head>"
        "<body>"
        f"<h1>{greeting}, {name}!</h1>"
        f"<p>Your email: {email}</p>"
        f"<p>Your comments: {comments}</p>"
        f"<p>Info: {user_info}</p>"
        "</body>"
        "</html>"
    )

    return render_template_string(template)

if __name__ == '__main__':
    port = 5555
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            print(f"Invalid port number: {sys.argv[1]}. Falling back to default port {port}.")

    app.run(host='0.0.0.0', port=port, debug=True)
