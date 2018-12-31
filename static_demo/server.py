"""
Test server for working with JS site.
"""
from flask import Flask, url_for, render_template

APP = Flask(__name__)


@APP.route('/index', methods=['GET'])
@APP.route('/', methods=['GET'])
def index():
    return "Welcome!"

@APP.route('/test', methods=['GET'])
def static_page(message="The Flask Store"):
    return render_template("test.html", message=message)

if __name__ == "__main__":
    APP.run(debug=True, host='0.0.0.0')
