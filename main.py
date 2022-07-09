from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route("/<name>")
def hello_world(name):
    return f"<p>Hello, {escape(name)}</p>"

@app.route("/")
def index():
    return f"<p>Index Page</p>"
