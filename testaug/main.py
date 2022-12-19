from testaug import test
from flask import Blueprint, render_template, request, url_for
import pandas as pd

main = Blueprint('main', __name__)

# we collect gpt-3 responses here
arr = []

# A negative sentiment sentence with negative sentiment question and word yes as the answer.
# A positive sentiment sentence with positive sentiment question and word yes as the answer.
# My opinion is more important than others’ when expressing positive sentiment.


@main.route('/', methods=["POST", "GET"])
def index():
    request_method = request.method
    error = []

    if request.method == 'POST':
        if "statement" in request.form:
            temp = []
            value = request.form['statement']
            value = value.split('\n')
            print(value)
            temp.append(value)
            # if len(value) < 10:
            #     error.append("The sentence must be at least 10 characters")
            #     return render_template('index.html', error=error)
            out = "hell"
            while len(out) != 5:
                out = test.generate_gpt3_test_suite(temp)

            for i in range(0, 5):
                out[i] = out[i].replace('["', ' ').replace(
                    "['", ' ').replace("']", ' ').replace(
                    '"]', ' ').replace('[', ' ').replace(
                    ']', ' ').replace(" , ", ' ').replace(
                    "', '", ' ').replace(",", ' ').replace(
                    ", ", ' ').replace('" "', ' ').replace(
                    "' '", ' ').replace('"', '').replace("'", '')
            print(out)
            value = ''.join(value)

        else:
            value = 0
        if "output" in request.form:
            user_like = request.form.getlist('output')
            arr.append(user_like)
        else:
            user_like = 0
        if value == 0:
            return render_template('index.html', request_method=request_method, user_like=user_like)
        if user_like == 0:
            return render_template('index.html', label=value, request_method=request_method, output=out)
        if user_like == 0 and value == 0:
            return render_template('index.html', request_method=request_method)
        return render_template('index.html', label=value, request_method=request_method, output=out, user_like=user_like)
    return render_template('index.html', request_method=request_method)


@main.route('/profile')
def profile():
    return render_template('profile.html')


# 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
# anotation is user decide
