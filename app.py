from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'codebaseAlpha 1.0.52-2 says Hello, Docker!'
