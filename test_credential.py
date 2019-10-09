import unittest
from credential import Credentials
import pyperclip

class TestUser(unittest.TestCase):
    def setUp(self):
        """
        method to run before each test

        """
        # instantiate an object by populating with dummy values.
        self.new_credential = Credentials("MySpace", "Ghostke99", "daimaMkenya001") 
    
    def tearDown(self):
        """
        this clears up data after each test to allow new entry of fresh data

        """
        Credentials.credential_list = []

    def test_init(self):
        """
        subject test for intialization
        
        """
        self.assertEqual(self.new_credential.app_name, "MySpace")
        self.assertEqual(self.new_credential.account_name, "Ghostke99")
        self.assertEqual(self.new_credential.account_password, "daimaMkenya001")


if __name__ == '__main__':
    unittest.main()
