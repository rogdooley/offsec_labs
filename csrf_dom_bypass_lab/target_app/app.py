from flask import Flask, request, render_template, jsonify

app = Flask(__name__)
USER_DB = {'email': 'user@example.com'}

@app.route("/")
def index():
    return render_template("change_email.html", email=USER_DB['email'])

@app.route("/api/update-email", methods=["POST"])
def update_email():
    token = request.headers.get("X-CSRF-Token")
    if token != "securetoken123":
        return "Invalid CSRF token", 403

    new_email = request.json.get("email")
    if new_email:
        USER_DB['email'] = new_email
        return jsonify({"status": "Email updated", "new": new_email})
    return "Missing email", 400

if __name__ == '__main__':
    app.run(debug=True)
