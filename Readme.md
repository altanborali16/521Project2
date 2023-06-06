First download repo to your local
Open command prompt or if you are using vs code use terminal but use command prompt option
Run => py -m venv env  
To active env run => env\Scripts\activate.bat 
Now your location should start with (env)
Run => pip3 install django (only need once)
Run => pip install pyodbc (only need once)
Run => pip install django-mssql-backend (only need once)

-- django-admin startproject Project2 (Already done no need to run)

-- python manage.py startapp Project2_app (Already done no need to run)

Run => python manage.py runserver

Run => pip3 install django-crispy-forms

------------------------------

Requirements : 
Python               3.7.9
asgiref              3.6.0
crispy-bootstrap4    2022.1
Django               3.2.19
django-crispy-forms  2.0
django-mssql-backend 2.8.1
numpy                1.21.6
pandas               1.3.5
pip                  20.1.1
pyodbc               4.0.39
python-dateutil      2.8.2
pytz                 2023.3
setuptools           47.1.0
six                  1.16.0
sqlparse             0.4.4
typing-extensions    4.5.0

------------------------------


-------------------------------------------------------
To start it each time
To active env run => env\Scripts\activate.bat
Run => python manage.py runserver
-------------------------------------------------------

-----------------------------------------------------------------------------------------------------
Project2/settings.py line starting 89 change settings according to your database

DATABASES = {
    'default': {
        'ENGINE': 'sql_server.pyodbc',
        'NAME': 'MovieDB',
        'USER': '',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',

        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',
        },
    },
}

Also Project2_app/dbConnection.py line starting 6 change information according to your database
conn_str = (
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=localhost;'
    'DATABASE=MovieDB;'
    'Trusted_Connection=yes;'
    )

To check driver 
py manage.py shell
import os, sys
import pyodbc
for driver in pyodbc.drivers():
    print(driver)

-----------------------------------------------------------------------------------------------------


