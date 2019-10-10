import string
import random
import pyperclip
import secrets


class Credentials:
    """
    #this class creates an instance of a user-credentials

    """
    credentials_list = []  # set an empty array of expected credentials.

    def __init__(self, app_name, account_name, account_password):

        """
        #user credentials parsing

        """
        self.app_name = app_name
        self.account_name = account_name
        self.account_password = account_password

    def credential_create(self):
        #create credentials  the populate credentials_list
        Credentials.credentials_list.append(self)

    def credential_remove(self):
        #remove credential from credentials_list
         Credentials.credentials_list.remove(self)

    @classmethod
    def search_name(cls, name):
            '''
            #search method to parse in name and return credentials matching 
                the name.
        
            '''
            for credentials in cls.credentials_list:
                if credentials.app_name == name:
                    return credentials

    @classmethod
    def search_duplicate(cls, appname):
        '''
        #confirm to check availability of name to prevent duplicate

        '''
        for Credentials in cls.credentials_list:
            if Credentials.app_name == appname:
                return True
        return False

    @classmethod
    def credentials_show(cls):
        '''
        #display list of creditials

        '''
        return cls.credentials_list

    @classmethod
    def copycat(cls, appname):
        """
        #method to allow copying of the credentials by user

        """
        #pyperclip module allows copy pasting
        credentials_copy = Credentials.search_name(cls)
        pyperclip.copy(credentials_copy.account_password)
        
