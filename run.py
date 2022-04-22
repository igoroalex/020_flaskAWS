"""
Run App
"""
from app.main import create_app
# from flask import Flask

# app = Flask(__name__)


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)


# @app.route("/")
# def hello_world():
#     return "<p>Hello, World 19 !</p>"


# if __name__ == "__main__":
#     app.run()
