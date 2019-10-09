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

    def test_init(self):
        """
        subject test for intialization

        """
        self.assertEqual(self.new_user.first_name, "mary")
        self.assertEqual(self.new_user.last_name, "mbugua")
        self.assertEqual(self.new_user.user_name, "nish")
        self.assertEqual(self.new_user.phone_number, "0789755096")
        self.assertEqual(self.new_user.email, "mary@gmail.com")
        self.assertEqual(self.new_user.password, "lovepy")
    
     
if __name__ == '__main__':
    unittest.main()
