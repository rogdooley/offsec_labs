from flask import Flask, request, render_template_string
import sys

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name', 'Guest')
        forbidden ="{}[].|"
        for char in forbidden:
            name = name.replace(char, '')
            template = f"{{{{ {name} }}}}"
        return render_template_string(template)
    return '''
        <form method="POST">
            <input name="name" placeholder="Enter your name">
            <input type="submit" value="Submit">
        </form>
    '''

if __name__ == '__main__':

    port = 5555

    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            print(f"Invalid port number: {sys.argv[1]}. Falling back to default port {port}.")

    app.run(host='0.0.0.0', port=port, debug=True)
