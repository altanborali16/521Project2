import pyodbc
from Project2_app.dbConnection import *

def checkCreditentials(username, password):
    GetUsers()
    return CheckUserExist(username,password)
    
    # if(user['Name'] != None and user['Name'] != '' and user['Name'] != []):
    #     return True
    # return False
    # if((user.name == "oyku" and surname == "yilmaz") or (name == "selen" and surname == "parlar")):
    #     return True
    # return False 