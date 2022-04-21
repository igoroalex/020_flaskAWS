from flask import Flask

app = Flask(__name__)


def create_app():
    return app


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
