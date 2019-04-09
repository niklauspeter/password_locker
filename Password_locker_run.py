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
	checking_user = Credential.check_user(first_name,password)
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
