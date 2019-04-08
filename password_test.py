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

    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            User.user_list = []



    def test_save_user(self):
        '''
        test case to see if user object is saved into the user_list
        '''
        self.new_user.save_user() #saving the new user_list
        self.assertEqual(len(User.user_list), 1)


    def test_save_multiple_user(self):
        '''
         to check if we can save multiple user
        objects to our contact_list
        '''

        self.new_user.save_user()
        test_user = User("test","user","babigando") # new contact
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)

    def delete_user(self):
        '''
        delete user method deletes a saved user from user user_list
        '''
        User.user_list.remove(self)


if __name__ == '__main__':
    unittest.main()
