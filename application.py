"""
Run App
"""
from flask import Flask
# from app.main import create_app
#
# application = create_app()
application = Flask(__name__)


@application.route("/")
def hello_world():
    return "<p>Hello, World112!</p>"


if __name__ == "__main__":
    application.run()
#     # app.run(debug=settings.DEBUG, port=settings.PORT, host=settings.HOST)


# EB looks for an 'application' callable by default.



# run the app.
# if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    # application.debug = True
    # application.run()
