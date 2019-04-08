import unittest
from user_class import User

class TestUser(unittest.TestCase):

    def setUp(self):
        '''
        set up method to run before each test caseself.
        '''
        self.new_user = User("klaus","peter","abracadabra")#creates new object

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.first_name,"klaus")
        self.assertEqual(self.new_user.last_name,"peter")
        self.assertEqual(self.new_user.password,"abracadabra")



if __name__ == '__main__':
    unittest.main()
