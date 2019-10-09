import unittest
from user import User
import pyperclip

class TestUser(unittest.TestCase):
    def setUp(self):
        """
        method to run before each test

        """
        # instantiate an object by populating with dummy values.
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
        self.assertEqual(self.new_user.first_name, "Wayne")
        self.assertEqual(self.new_user.last_name, "Ghost")
        self.assertEqual(self.new_user.user_name, "OGhost")
        self.assertEqual(self.new_user.phone_number, "0724443879")
        self.assertEqual(self.new_user.email, "oghost@gmail.com")
        self.assertEqual(self.new_user.password, "daimaMkenya001")
     
    def test_user_create(self):
        """ 
        #determine is the user list is populated and details saved
        
        """
        self.new_user.user_create()
        self.assertEqual(len(User.user_list),1)

    def test_user_show(self):
        """
        #test method to display users
        
        """
        self.assertEqual(User.user_show(), User.user_list)
     
if __name__ == '__main__':
    unittest.main()
