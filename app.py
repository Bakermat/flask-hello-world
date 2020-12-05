from flask import Flask, request
app = Flask(__name__)

@app.route('/', methods=["GET"])
def get_my_ip():
    return f'Your IP is: {request.remote_addr}', 200
