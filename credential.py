import string
import random
import pyperclip
import secrets


class User:
    """
    #this class creates an instance of a user-credentials

    """
    credentials_list = []  # set an empty array of expected credentials

    def __init__(self, app_name, account_name, account_password):
