from flask import Flask, request
app = Flask(__name__)

@app.route('/', methods=["GET"])
def root():
    return f'Hello World!', 200

@app.route('/ip', methods=["GET"])
def get_my_ip():
    return f'Your IP is: {request.remote_addr}', 200

@app.route('/error', methods=["GET"])
def error():
    return f'Fake Auth Error', 502
