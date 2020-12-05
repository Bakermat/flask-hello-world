from flask import Flask, request
app = Flask(__name__)

@app.route('/', methods=["GET"])
def root():
    return f'Welcome to our website!!', 200

@app.route('/ip', methods=["GET"])
def ip():
    return f'Your IP is: {request.remote_addr}', 200

@app.route('/store', methods=["GET"])
def store():
    return f'Welcome to the store!', 200

@app.route('/error', methods=["GET"])
def error():
    return f'Fake Authentication Error!', 502
