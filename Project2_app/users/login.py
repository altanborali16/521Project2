import pyodbc
from Project2_app.dbConnection import *

def checkCreditentials(name, surname):
    # conn_str = (
    # 'DRIVER={ODBC Driver 17 for SQL Server};'
    # 'SERVER=localhost;'
    # 'DATABASE=MovieDB;'
    # 'Trusted_Connection=yes;'
    # )
    # db = pyodbc.connect(conn_str)
    # cnn = db.cursor()
    # cnn.execute('SELECT * FROM USERS')
    # users = cnn.fetchall()
    # for i in users:
    #     print(i)
    # db.close()
    GetUsers()
    CheckUserExist(name,surname)
    if((name == "oyku" and surname == "yilmaz") or (name == "selen" and surname == "parlar")):
        return True
    return False 