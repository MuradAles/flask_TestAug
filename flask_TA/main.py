from flask import Blueprint, render_template

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/profile')
def profile():
    return render_template('profile.html')


# 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
# anotation is user decide