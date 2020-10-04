from flask import Flask, render_template, request, url_for, redirect
from program_functions import *
import json

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        data = request.form.to_dict()
        approval = approve_deny_transaction(data)
        if approval == 'approve':
            authorization_code = create_authorization_code()
            return authorization_code
        else:
            return 'Declined'
        return data
    else:
        return render_template('payment.html')


@app.route("/approved")
def processed_payment(data):
    return f"<h2>{data}</h2>"


@app.route("/declined")
def error():
    return render_template('error.html')


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)
