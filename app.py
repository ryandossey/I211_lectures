from flask import Flask
app = Flask(__name__)

@app.route('/')
def helllo_world():
    return 'Hello, World!'