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
        """
        #user details parsing

        """
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.phone_number = phone_number
        self.email = email
        self.password = password 
    
    def user_create(self):
        User.user_list.append(cls):
    
    @classmethod
    def user_show(cls):
        """
        method to display users
    
        """
        return cls.user_list
    
    def passcode_generate():
        """
        #this method auto-generates a passcode for the user following
            guidelines on character randomization where uppercase,lowercase,
                symbols are used to get a EIGHT character passcode.

        """
        #pascode is mutated to create an uppercase,lowercase,string and symbols characters
        characters = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation

        #to generate the passcode of length
        passlength = random.randint(8, 16)
        

