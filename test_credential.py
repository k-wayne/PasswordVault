import unittest
from credential import Credentials
import pyperclip

class TestUser(unittest.TestCase):
    def setUp(self):
        """
        #method to run before each test

        """
        # instantiate an object by populating with dummy values.
        self.new_credential = Credentials("MySpace", "Ghostke99", "daimaMkenya001") 
    
    def tearDown(self):
        """
        #this clears up data after each test to allow new entry of fresh data

        """
        Credentials.credentials_list = []

    def test_init(self):
        """
        #subject test for intialization
        
        """
        self.assertEqual(self.new_credential.app_name, "MySpace")
        self.assertEqual(self.new_credential.account_name, "Ghostke99")
        self.assertEqual(self.new_credential.account_password, "daimaMkenya001")

    def test_credential_create(self):
        """
        #determine is the credential list is populated and details saved

        """
        self.new_credential.credential_create()
        self.assertEqual(len(Credentials.credentials_list), 1)

    def test_deletecredential(self):
        """
        #remove populated credentials

        """
        self.new_credential.credential_create()
        test_credentials = Credentials("MySpace", "Ghostke99", "daimaMkenya001")
        test_credentials.credential_create()
        self.new_credential.credential_remove()
        self.assertEqual(len(Credentials.credentials_list), 1)

    def test_search_duplicate(self):
        """
        #test confirm to check availability of name to prevent duplicate

        """
        self.new_credential.credential_create()
        test_credentials = Credentials("MySpace", "Ghostke99", "daimaMkenya001")
        test_credentials.credential_create()
        search_duplicate = Credentials.search_duplicate("MySpace")
        self.assertTrue(search_duplicate)

if __name__ == '__main__':
    unittest.main()
