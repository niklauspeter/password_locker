
import random
import string


global user_list

class User:
    user_list= []
    def __init__(self, first_name,last_name, password ):

        self.first_name= first_name
        self.last_name=last_name
        self.password= password
        '''
        __init__ method helps define properties for our objectsself.

        Args:
            first_name: New user first nameself.
            last_name: New user last nameself.
            password: New user password.
        '''
    def save_user(self):
        '''
        save user method to add new user instance to list.
        '''
        User.user_list.append(self)

    def delete_user(self):
        '''
        delete user method deletes a saved user from user user_list
        '''
        User.user_list.remove(self)

class Credential:

	'''
	Class that creates account credentials, generates passwords and saves user information
	'''
	credential_list =[]
	user_credentials_list = []
	@classmethod
	def user_check(cls,first_name,password):
		'''
		Method that checks if the name and password entered are same as those in the users_list
		'''
		current_user = ''
		for user in User.users_list:
			if (user.first_name == first_name and user.password == password):
				current_user = user.first_name
		return current_user

    def __init__(self,user_name,site_name,account_name,password):

        self.user_name =user_name
        self.site_name= site_name
        self.account_name= account_name
        self.password= password

    def save_credentials(self):
        '''
        Function that saves a newly created credential instance
        '''
        credential.credential_list.append(self)

    def generate_password(size=8, char=string.ascii_uppercase+string.ascii_lowercase+string.digits):
		'''
		Function to generate an 8 character password for a credential
		'''
		gen_password=''.join(random.choice(char) for _ in range(size))
		return gen_password
