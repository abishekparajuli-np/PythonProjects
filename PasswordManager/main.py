from cryptography.fernet import Fernet
import random
import string

# def write_key():
#     key=Fernet.generate_key()
#     with open("key.key",'wb') as _keyFile:
#         _keyFile.write(key)
# write_key()
# _masterPwd = input("What is the master password?: ")
def get_random_password(length=12):
    _randomPwd= string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choices(_randomPwd, k=length))
def _verification():
    password="Abishek"
    attempt= input("what is the master password?")
    return attempt == password

_isAuthenticated=_verification()

def load_key():
    with open('key.key','rb') as f:
        key=f.read()
        return key

key=load_key()
fer=Fernet(key)

class mode:
    def __init__(self,_mode):
        self._mode=_mode
    
    def _choice(self):
        if self._mode=='view':
            mode.view()
        elif self._mode=='add':
            mode.add()
        else:
            print("Invalid Input!!")
    
    def view():
        print("You Choose To Add View")
        _accountName=input("Enter Account Name: ")
        if not _isAuthenticated:
            print("Account: {}\nPassword: {}".format(_accountName,get_random_password()))
        else:
            try:
                with open('password.txt','r') as f:
                    for line in f.readlines():
                        data=line.rstrip()
                        if " | " not in data:
                            continue
                        user,passw=data.split(" | ")
                        if user==_accountName:
                            decrypted=(fer.decrypt(passw.encode())).decode()
                            print("Account: {}\nPassword: {}".format(user,decrypted))
                        else:
                            print("Account Not Found!!!")
            except OSError as e:
                print("Error Reading the Data",e)
    
    def add():
        print("You Choose To Add Data")
        _accountName=input("Enter Account Name: ")
        _pwd=input("Enter Password: ")
        if not _isAuthenticated:
            print("Password Added Successfully")
        else:
            try:
                with open('password.txt','a') as f:
                    f.write(_accountName+ " | " + (fer.encrypt(_pwd.encode())).decode()+'\n')
                    print("Password Added Successfully")
            except OSError as e:
                print("Failed To Add Password!!!",e)
            
while True:
    _mode = input("Would you like to add a new password or view a existing ones(view/add). press 'q' to exit: ").lower()
    if _mode == 'q':
        break
    _opt = mode(_mode)
    _opt._choice()
    




