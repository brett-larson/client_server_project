from flask import Flask, render_template, request, url_for, redirect
from program_functions import *

# Creating the Flask application
app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def main():
    """
    This function serves the main credit card webpage. It provides for GET and POST requests.
    It accepts data and calls additional functions to determine if the transaction is approved
    or declined.
    :return: approval or declined webpage based on user input.
    """
    if request.method == 'POST':
        data = request.form.to_dict()
        approval = approve_deny_transaction(data)
        last_four_num = mask_credit_card(data)
        if approval == 'approve':
            authorization_code = create_authorization_code()
            return render_template('approved.html', authorization_code=authorization_code,
                                   last_four_num=last_four_num)
        else:
            return render_template('declined.html', last_four_num=last_four_num)
    else:
        return render_template('payment.html')


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)
