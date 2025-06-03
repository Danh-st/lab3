# save this as app.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"
@app.route("/api")
def api():
    return "Hello, World!"
