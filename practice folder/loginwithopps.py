# login user auth with user name pass
user_username = input('enter your username :')
user_password = input(' enter your password:')


class user:


    def __init__(self , username , password):
        self.username = username
        self.password = password
    

    def get_password(self):
        return self.password


class auth(user):

    def __init__(self , username , password):
        super().__init__(username , password)

    def login(self ,username , password):
        if username == self.username and password == self.password:
            return "loggged iN" + self.username + " " + self.password + " " + username + " " + password
        else:
            return "failed " + self.username + " " + self.password + " " + username + " " + password

    def reg():
        pass

obj = auth('kushal', '123')

print(obj.login(user_username,user_password))




from abc import ABC , abstractmethod

class Human(ABC):
    @abstractmethod
    def talk(self):
        print("talking")