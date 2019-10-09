import unittest
from user import User
import pyperclip

class TestUser(unittest.TestCase):
    def setUp(self):
        """
        method to run before each test

        """
        # instantiate an object
        self.new_user = User("Wayne", "Ghost", "OGhost", "0724443879","oghost@gmail.com", "daimaMkenya001") 
    
    def tearDown(self):
        """
        this clears up data after each test to allow new entry of fresh data

        """
        User.user_list = []
    
     
