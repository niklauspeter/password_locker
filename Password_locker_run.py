#! /usr/bin/env python3
import pyperclip
from user_class import User, Credential

def createNewUser(fname,lname, password):
    '''
    Function that creates a new user account
    '''
    new_user= User(fname, lname, password)
    return new_user

def save_user
