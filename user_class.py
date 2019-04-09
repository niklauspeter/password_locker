
import pyperclip
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

	def __init__(self,user_name,site_name,account_name,password):
		
		self.user_name = user_name
		self.site_name= site_name
		self.account_name= account_name
		self.password= password
	
	@classmethod
	def user_check(cls,first_name,password):
		'''
		Method that checks if the name and password entered are same as those in the users_list
		'''
		current_user = ''
		for user in User.user_list:
			if (user.first_name == first_name and user.password == password):
				current_user = user.first_name
		return current_user
		
		
	def save_credentials(self):
		
		'''
		Function that saves a newly created credential instance
        '''
		Credential.credential_list.append(self)
		
	def generate_password(size=8, char=string.ascii_uppercase+string.ascii_lowercase+string.digits):
		'''
		Function to generate an 8 character password for a credential
		'''
		gen_password=''.join(random.choice(char) for _ in range(size))
		return gen_password
		
	@classmethod
	def display_credentials(cls,user_name):
		'''
		a method meant to display credentials
		'''
		user_credentials_list = []
		for credential in cls.credential_list:
			if credential.user_name == user_name:
				user_credentials_list.append(credential)
		return user_credentials_list
		
	@classmethod
	def find_by_site_name(cls, site_name):
		'''
		Method that returns credentials by taking in the site name
		'''
		for credential in cls.credential_list:
			if credential.site_name == site_name:
				return credential
				
	@classmethod
	def copy_credential(cls,site_name):
		'''
		Class method that copies a credential's info after the credential's site name is entered
		'''
		find_credential = Credential.find_by_site_name(site_name)
		return pyperclip.copy(find_credential.password)
