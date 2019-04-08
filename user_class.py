class User:
    def __init__(self, first_name,last_name, password ):
        user_list= []


        '''
        __init__ method helps define properties for our objectsself.

        Args:
            first_name: New user first nameself.
            last_name: New user last nameself.
            password: New user password.
        '''
        self.first_name= first_name
        self.last_name=last_name
        self.password= password
