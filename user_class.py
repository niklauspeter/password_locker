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
        save user method
        '''
        User.user_list.append(self)

    def delete_user(self):
        '''
        delete user method deletes a saved user from user user_list
        '''
        User.user_list.remove(self)
