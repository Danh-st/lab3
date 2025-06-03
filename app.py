# save this as app.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"
@app.route("/api")
def api():
    return "Hello, World!"
app.run(host="0.0.0.0", port=10000)
