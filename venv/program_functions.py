# required imports
import json
import random
import string


def post_json_to_dictionary(post_data):
    data_set = json.load(post_data)
    
    return data_set

def create_authorization_code():
    """
    Create an authorization code through the creation of a string of random letters and numbers
    :return: string authorization code
    """
    letters_numbers = string.ascii_letters + string.digits
    authorization_code = ''.join((random.choice(letters_numbers) for i in range(10)))

    return authorization_code

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