import string
import random
import pyperclip
import secrets

class User:
    """
    #this class creates an instance of a user
    """
    user_list = [] #set an empty array of expected users

    def __init__(self, first_name, last_name, user_name, phone_number, email, password):
