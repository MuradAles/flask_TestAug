from flask_TA.functions import python_functions
from flask import Blueprint, render_template, request, url_for
main = Blueprint('main', __name__)


@main.route('/', methods=["POST", "GET"])
def index():
    request_method = request.method
    if request.method == 'POST':
        value = request.form['statement']
        num = python_functions.displayText(4)
        return render_template('index.html', label=value, request_method=request_method, number=num)
    return render_template('index.html', request_method=request_method)


@main.route('/profile')
def profile():
    return render_template('profile.html')


# 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
# anotation is user decide
