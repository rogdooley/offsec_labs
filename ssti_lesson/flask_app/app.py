from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name', 'Guest')
        template = f"Hello, {name}!"
        return render_template_string(template)
    return '''
        <form method="POST">
            <input name="name" placeholder="Enter your name">
            <input type="submit" value="Submit">
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)
