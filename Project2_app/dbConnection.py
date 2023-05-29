import pyodbc
from django.db import connection
import pandas as pd
import json

conn_str = (
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=localhost;'
    'DATABASE=MovieDB;'
    'Trusted_Connection=yes;'
    )
def query_db(query, args=(), one=False):
    db = pyodbc.connect(conn_str)
    cur = db.cursor()
    cur.execute(query, args)
    r = [dict((cur.description[i][0], value) \
               for i, value in enumerate(row)) for row in cur.fetchall()]
    cur.connection.close()
    return (r[0] if r else None) if one else r

def GetUsers():
    query = 'SELECT * FROM USERS'
    users =  query_db(query)
    return users

def GetDirectors():
    query = 'SELECT * FROM Directors'
    directors =  query_db(query)
    return directors

def CheckUserExist(username,password):
    
    query = (f"SELECT name FROM Users WHERE username ='{username}' and password ='{password}'")
    users =  query_db(query)
    print(users)
    if(len(users) <= 0):
        return False
    return True
    

    # for user in users:
    #     if (user['name'] != None and user['name'] != '' and user['name'] != []):
    #         return True
    # return False

def CheckUserDatabaseManager(username,password):

    query = (f"SELECT username FROM DataBaseManager WHERE username ='{username}' and password ='{password}'")
    dbmanagers =  query_db(query)
    print(dbmanagers)
    if(len(dbmanagers) <= 0):
        return False
    return True

    # for user in dbmanagers:
    #     if (user['username'] != None and user['username'] != '' and user['username'] != []):
    #         return True
    # return False

def CheckUserDirector(username):
    query = (f"SELECT director_username FROM Directors WHERE director_username ='{username}'")
    directors =  query_db(query)
    print(directors)
    print("Directors count : ", len(directors)) 
    if(len(directors) <= 0):
        return False
    return True
    # for user in directors:
    #     if (user['director_username'] != None and user['director_username'] != '' and user['director_username'] != []):
    #         return True
    # return False

def AddUser(username,password,name,surname):
    query = (f"INSERT INTO Users (username, password, name, surname) VALUES ('{username}', '{password}', '{name}','{surname}')")
    print(query)
    db = pyodbc.connect(conn_str)
    cur = db.cursor()
    cur.execute(query)
    cur.commit()
    # cur.connection.close()
    print("User Ekledi")

def AddAudience(username):
    query = (f"INSERT INTO Audiences (audience_username) VALUES ('{username}');")
    db = pyodbc.connect(conn_str)
    cur = db.cursor()
    cur.execute(query)
    cur.commit()
    # cur.connection.close()
    print("Audience Ekledi")
def DeleteUser(username):
    query = (f"Delete from Users where username ='{username}'")
    db = pyodbc.connect(conn_str)
    cur = db.cursor()
    cur.execute(query)
    cur.commit()
    # cur.connection.close()
    print("Audience Silindi")


        
