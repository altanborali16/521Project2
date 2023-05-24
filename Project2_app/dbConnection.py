import pyodbc

conn_str = (
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=localhost;'
    'DATABASE=MovieDB;'
    'Trusted_Connection=yes;'
    )

def GetUsers():
    db = pyodbc.connect(conn_str)
    cnn = db.cursor()
    cnn.execute('SELECT * FROM USERS')
    users = cnn.fetchall()
    for i in users:
        print(i)
    db.close()

def CheckUserExist(username,password):
    user = []
    db = pyodbc.connect(conn_str)
    cnn = db.cursor()
    # cnn.execute("SELECT EXISTS (SELECT * FROM Users WHERE username ='"+ username +"' and password ='"+ password + "')")
    cnn.execute("SELECT * FROM Users WHERE username ='"+ username +"' and password ='"+ password + "'")
    # cnn.execute("SELECT * FROM users WHERE username = '{username}' AND password = '{password}'")
    output = cnn.fetchall()
    print(output)
    for i in output:
        print(i)

        
