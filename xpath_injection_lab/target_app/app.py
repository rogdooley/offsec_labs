import os
import logging
import base64
import argparse


from flask import Flask, request, redirect, render_template, session, abort, flash
from lxml import etree

app = Flask(__name__)

# Base directory for file serving and directory listing
BASE_DIRECTORY = os.getcwd()

log_path = os.path.join(BASE_DIRECTORY, "requests.log")

logging.basicConfig(
    filename=log_path,
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logging.info("Logging system initialized.")

app.secret_key = 'some-secret'

@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return "Hi!"


@app.route('/login', methods=['POST'])
def login():
    password = request.form['password']
    username = request.form['username']
    logging.info(f"Raw input - username: {username}, password: {password}")

    tree = etree.parse("users.xml")

    xpath_query = f".//user[username/text()='{username}' and password/text()='{password}']"
    logging.info(f"XPath query: {xpath_query}")
    result = tree.xpath(xpath_query)
    logging.info(f"XPath result: {result}")

    if result:
        session['logged_in'] = True
        return "Login successful", 200
    else:
        abort(401)



if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Flask HTTP Server with optional SSL.')
    parser.add_argument('--port', type=int, default=8080, help='Port number to listen on.')
    parser.add_argument('--dir', type=str, default=BASE_DIRECTORY, help='Base directory to serve files from.')
    parser.add_argument('--ssl', action='store_true', help='Enable SSL using cert.pem and key.pem.')
    args = parser.parse_args()

    BASE_DIRECTORY = args.dir
    print(f"Starting Flask server on port {args.port}...")
    print(f"Logging requests to requests.log")
    print(f"Serving files from {BASE_DIRECTORY}")
    if args.ssl:
        print("SSL enabled with cert.pem and key.pem")
        context = ('cert.pem', 'key.pem')
        app.run(host='0.0.0.0', port=args.port, ssl_context=context)
    else:
        app.run(host='0.0.0.0', port=args.port)

