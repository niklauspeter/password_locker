#! /usr/bin/env python3
import pyperclip
from user_class import User, Credential

def createNewUser(fname,lname, password):
    '''
    Function that creates a new user account
    '''
    new_user= User(fname, lname, password)
    return new_user

def saveUser(user):
    '''
    function that saves new user account instance
    '''
    User.save_user(user)

def verifyUser(first_name,password):
	'''
	Function that verifies the existance of the user before creating credentials
	'''
	checking_user = Credential.user_check(first_name,password)
	return checking_user

def generatePassword():
	'''
	Function that automatically generates password for the user
	'''
	gen_pass = Credential.generate_password()
	return gen_pass

def createCredential(user_name,site_name,account_name,password):
	'''
	Function to create a new credential
	'''
	new_credential=Credential(user_name,site_name,account_name,password)
	return new_credential

def saveCredential(credential):
	'''
	Function to save a newly created credential
	'''
	Credential.save_credentials(credential)

def displayCredentials(user_name):
	'''
	Function to display credentials saved by a user
	'''
	return Credential.display_credentials(user_name)

def copyCredential(site_name):
	'''
	Function to copy a credentials details to the clipboard
	'''
	return Credential.copy_credential(site_name)

def main():
	print(' ')
	print('Hello! Welcome to Password Locker.')
	while True:
		print(' ')
		print("-"*60)
		print('Use these codes to navigate: \n ca-Create an Account \n li-Log In \n ex-Exit')
		short_code = input('Enter a choice: ').lower().strip()
		if short_code == 'ex':
			break
		
		elif short_code == 'ca':
			print("-"*60)
			print(' ')
			print('To create a new account:')
			first_name = input('Enter your first name - ').strip()
			last_name = input('Enter your last name - ').strip()
			password = input('Enter your password - ').strip()
			saveUser(createNewUser(first_name,last_name,password))
			print(" ")
			print(f'New Account Created for: {first_name} {last_name} using password: {password}')

				


			
if __name__ == '__main__':
	main()