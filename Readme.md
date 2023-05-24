First download repo to your local
Open command prompt or if you are using vs code use terminal but use command prompt option
Run => py -m venv env  
To active env run => env\Scripts\activate.bat 
Now your location should start with (env)
Run => pip3 install django (only need once)
Run => pip install pyodbc
Run => pip install django-mssql-backend

-- django-admin startproject Project2 (Already done no need to run)

-- python manage.py startapp Project2_app (Already done no need to run)

Run => python manage.py runserver


Basically to start it each time
To active env run => env\Scripts\activate.bat (Also no need just checked)
Run => python manage.py runserver


Last written code on min 18

Run => pip3 install django-crispy-forms



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

To check driver 
py manage.py shell
import os, sys
import pyodbc
for driver in pyodbc.drivers():
    print(driver)

