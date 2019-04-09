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

		elif short_code == 'li':
			print("-"*60)
			print(' ')
			print('To login, please enter your account details:')
			user_name = input('Enter your first name - ').strip()
			password = str(input('Enter your password - '))
			user_exists = verifyUser(user_name,password)
			if user_exists == user_name:
				print(" ")
				print(f'Welcome {user_name}. Choose an option to continue.')
				print(' ')
				while True:
					print("-"*60)
					print('Navigation codes: \n cc-Create a Credential \n dc-Display Credentials \n cpy-Copy Password \n ex-Exit')
					short_code = input('Enter a choice: ').lower().strip()
					print("-"*60)
					if short_code == 'ex':
						print(" ")
						print(f'ByeBye {user_name}')
						break
					elif short_code == 'cc':
						print(' ')
						print('Enter your credential details:')
						site_name = input('Enter the site\'s name- ').strip()
						account_name = input('Enter your account\'s name - ').strip()
						while True:
							print(' ')
							print("-"*60)
							print('Choose an option to insert a password: \n ep-enter existing password \n gp-AUTOgenerate a password \n ex-exit')
							pwd_choice = input('Enter an option: ').lower().strip()
							print("-"*60)
							if pwd_choice == 'ep':
								print(" ")
								password = input('Enter your password: ').strip()
								break
							elif pwd_choice == 'gp':
								password = generatePassword()
								break
							elif pwd_choice == 'ex':
								break
							else:
								print('Wrong option entered.Please Try again.')
						saveCredential(createCredential(user_name,site_name,account_name,password))
						print(' ')
						print(f'Credential has been Created succcessfully: Site Name: {site_name} - Account Name: {account_name} - Password: {password}')
						print(' ')
					elif short_code == 'dc':
						print(' ')
						if displayCredentials(user_name):
							print('This is a list of all your credentials')
							print(' ')
							for credential in displayCredentials(user_name):
								print(f'Site Name: {credential.site_name} - Account Name: {credential.account_name} - Password: {credential.password}')
							print(' ')	
						else:
							print(' ')
							print("You don't seem to have any credentials saved yet")
							print(' ')
					elif short_code == 'cpy':
						print(' ')
						site_chosen = input('Enter the site name whose password you want to copy: ')
						copyCredential(site_chosen)
						print('')
					else:
						print('Wrong option entered.Please Try again.')

			else: 
				print(' ')
				print(' Wrong details entered. Please Try again or Create an Account.')		
		
		


if __name__=='__main__':
	
	main()

