# required imports
import json
import random
import string


def create_authorization_code():
    """
    Create an authorization code through the creation of a string of random letters and numbers
    :return: string authorization code
    """
    letters_numbers = string.ascii_letters + string.digits
    authorization_code = ''.join((random.choice(letters_numbers) for i in range(10)))

    return authorization_code

def mask_credit_card(data_set):
    """
    Take the credit card number provided by the user, and truncate it to the last four numbers.
    :param data_set: Dictionary provided by the customer
    :return: String containing the last four digits of the credit card number
    """

    credit_card_num = data_set.get('card_number')
    last_four_num = credit_card_num[-4:]
    
    return last_four_num


def approve_deny_transaction(data_set):
    """
    This function approves transactions with a purchase value of less than 200 and greater than 0.
    :param data_set: JSON PUT data stored in a dictionary
    :return: string "approve" or "decline"
    """
    approval = 'approve'

    amount = int(data_set.get('purchase_amt'))

    if amount >= 200 or amount <= 0:
        approval = 'decline'

    return approval