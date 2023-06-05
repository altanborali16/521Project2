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

def GetAudiences():
    users = GetUsers()
    query = 'SELECT * FROM Audiences'
    audiences = query_db(query)
    data = []
    for user in users:
        isaudience = False
        for audience in audiences:
            if user['username'] == audience['audience_username']:
                isaudience = True
        
        if isaudience:
            data.append({
                'username': user['username'],
                'password': user['password'],
                'name': user['name'],
                'surname': user['surname']
            })
    
    return data

def GetDirectors():
    users = GetUsers()
    query = 'SELECT * FROM Directors'
    directors =  query_db(query)
    data = []
    for user in users:
        isaudience = False
        username =""
        nation =""
        platformid =""
        for director in directors:
            if user['username'] == director['director_username']:
                isaudience = True
                username = director['director_username']
                nation = director['nation']
                platformid = director['platform_id']
        
        if isaudience:
            data.append({
                'director_username': username,
                'name': user['name'],
                'surname': user['surname'],
                'nation': nation,
                'platform_id': platformid
            })
    
    return data
    return directors

def CheckUserExist(username,password):
    
    query = (f"SELECT name FROM Users WHERE username ='{username}' and password ='{password}'")
    users =  query_db(query)
    # print(users)
    if(len(users) <= 0):
        return False
    return True

def CheckUserDatabaseManager(username,password):

    query = (f"SELECT username FROM DataBaseManager WHERE username ='{username}' and password ='{password}'")
    dbmanagers =  query_db(query)
    # print(dbmanagers)
    if(len(dbmanagers) <= 0):
        return False
    return True


def CheckUserDirector(username):
    query = (f"SELECT director_username FROM Directors WHERE director_username ='{username}'")
    directors =  query_db(query)
    # print(directors)
    # print("Directors count : ", len(directors)) 
    if(len(directors) <= 0):
        return False
    return True

def AddUser(username,password,name,surname):
    query = (f"INSERT INTO Users (username, password, name, surname) VALUES ('{username}', '{password}', '{name}','{surname}')")
    # print(query)
    db = pyodbc.connect(conn_str)
    cur = db.cursor()
    cur.execute(query)
    cur.commit()
    # cur.connection.close()
    # print("User Ekledi")

def AddAudience(username):
    query = (f"INSERT INTO Audiences (audience_username) VALUES ('{username}');")
    db = pyodbc.connect(conn_str)
    cur = db.cursor()
    cur.execute(query)
    cur.commit()
    # cur.connection.close()
    # print("Audience Ekledi")

def GetAudienceMovies(username):
    query = query = (f"SELECT * FROM MovieRating WHERE audience_username ='{username}'")
    movieRatings =  query_db(query)
    query = query = (f"SELECT * FROM Movies")
    movies =  query_db(query)
    data = []
    for movieRate in movieRatings:
        for movie in movies:
            if movieRate['movie_id'] == movie['movie_id']:
                data.append({
                    'audience_username': movieRate['audience_username'],
                    'movie_name': movie['movie_name'],
                    'movie_id': movie['movie_id'],
                    'rating': movieRate['rating'],
                })
    
    return data

def DeleteUser(username):
    query = (f"Delete from Users where username ='{username}'")
    db = pyodbc.connect(conn_str)
    cur = db.cursor()
    cur.execute(query)
    cur.commit()
    # cur.connection.close()
    # print("Audience Silindi")

def GetNations():
    query = 'SELECT * FROM Nations'
    nations =  query_db(query)
    # print (nations)
    return nations

def GetPlatforms():
    query = 'SELECT * FROM Platforms'
    platforms =  query_db(query)
    # print (platforms)
    return platforms

def GetMoviesWithRate():
    query1 = (f"SELECT * FROM MovieRating")
    movieRatings =  query_db(query1)
    query2 = (f"SELECT * FROM Movies")
    movies =  query_db(query2)
    data = []
    for movie in movies:
        rate_count = 0
        total_rate = 0
        for movieRate in movieRatings:
            if movieRate['movie_id'] == movie['movie_id']:
                rate_count += 1
                total_rate += movieRate['rating']
        avg = 0
        if rate_count > 0 :
            avg = total_rate/rate_count
        data.append({
            'movie_name': movie['movie_name'],
            'movie_id': movie['movie_id'],
            'overall_rating': avg,
        })
    
    return data

def GetDirectorMovieSessions(director_username):
    query1 = (f"SELECT * FROM Movies where director_username ='{director_username}'")
    movies =  query_db(query1)
    data = []
    for movie in movies:
        query2 = (f"SELECT * FROM Sessions where movie_id ='{movie['movie_id']}'")
        sessions = query_db(query2)
        # print("sessions : ", sessions)
        for session in sessions:
            query3 = (f"SELECT * FROM TheatreSessions where session_id ='{session['session_id']}'")
            theatresessions = query_db(query3)
            # print("theatresessions : ", theatresessions)
            for theatresession in theatresessions:
                query4 = (f"SELECT * FROM Theatres where theatre_id ='{theatresession['theatre_id']}'")
                theatres = query_db(query4)
                # print("theatres : ", theatres)
                for theatre in theatres:
                    data.append({
                        'movie_id': movie['movie_id'],
                        'movie_name': movie['movie_name'],
                        'theatre_id': theatre['theatre_id'],
                        'theatre_name': theatre['theatre_name'],
                        'time_slot': theatresession['time_slot'],
                        'district' : theatre['district'],
                        'date' : theatresession['date'],
                    })
    return data



def AddDirector(username,nation,platform_id):
    query = (f"INSERT INTO Directors (director_username, nation, platform_id) VALUES ('{username}', '{nation}', '{platform_id}')")
    # print(query)
    db = pyodbc.connect(conn_str)
    cur = db.cursor()
    cur.execute(query)
    cur.commit()


def UpdateDirector(director_username,platform_id):
    query = (f"UPDATE Directors SET platform_id = '{platform_id}' WHERE director_username = '{director_username}';")
    db = pyodbc.connect(conn_str)
    cur = db.cursor()
    cur.execute(query)
    cur.commit()

def GetTheatres():
    query = (f"SELECT * FROM Theatres")
    theatres =  query_db(query)
    return theatres
    
def GetDirectorInformation(director_username):
    query1 = (f"SELECT * FROM Directors where director_username ='{director_username}'")
    director =  query_db(query1)
    # print(director)
    query2 = (f"SELECT platform_name FROM Platforms where platform_id ='{director[0]['platform_id']}'")
    platform_name =  query_db(query2)
    # print(platform_name)
    director[0].update(platform_name[0])
    # print(director) 
    return director

def GetDirectorMoviesWithGenre(director_username):
    query = (f"SELECT * FROM Movies where director_username ='{director_username}'")
    directorMovies = query_db(query)
    # print(directorMovies)
    query1 = (f"SELECT * FROM Genres")
    genres = query_db(query1)
    for directorMovie in directorMovies:
        directorMovie['genre'] = ''
        directorMovie['predeccors'] = ''
        query = (f"SELECT * FROM MovieGenre where movie_id ='{directorMovie['movie_id']}'")
        directorGenres = query_db(query)
        for directorGenre in directorGenres:
            for genre in genres:
                if(directorGenre['genre_id'] == genre['genre_id']):
                    if not directorMovie['genre'] :
                        directorMovie['genre'] = genre['genre_name']
                    else : 
                        directorMovie['genre'] += " ," + genre['genre_name']
        query = (f"SELECT * FROM MoviePredeccors where movie_id ='{directorMovie['movie_id']}'")
        directorMoviePredeccors = query_db(query)
        for directorMoviePredeccor in directorMoviePredeccors:
            for directorMovie2 in directorMovies:
                if(directorMoviePredeccor['predeccors_id'] == directorMovie2['movie_id']):
                    if not directorMovie['predeccors'] :
                        directorMovie['predeccors'] = directorMovie2['movie_name']
                    else : 
                        directorMovie['predeccors'] += " ," + directorMovie2['movie_name']


    return directorMovies

def AddMovie(username,movieName,duration,genreID,genreID1,genreID2,genreID3):
    query = (f"SELECT TOP 1 * FROM Movies ORDER BY movie_id DESC")
    lastMovie = query_db(query)
    lastMovieId = lastMovie[0]['movie_id']
    # print("Last movie id : " , lastMovieId)
    newMovieId = lastMovieId + 1
    # print("New movie id : " , newMovieId)
    query = (f"INSERT INTO Movies (movie_id, movie_name, duration,director_username ) VALUES ('{newMovieId}', '{movieName}', '{duration}', '{username}')")
    db = pyodbc.connect(conn_str)
    cur = db.cursor()
    cur.execute(query)
    cur.commit()
    # Movie Genre add
    genre_list = [80001, 80002, 80003, 80004,80005,80006]
    if genreID in genre_list:
        query1 = (f"INSERT INTO MovieGenre (movie_id, genre_id ) VALUES ('{newMovieId}', '{genreID}')")
        db = pyodbc.connect(conn_str)
        cur = db.cursor()
        cur.execute(query1)
        cur.commit()
    if genreID1 in genre_list:
        query2 = (f"INSERT INTO MovieGenre (movie_id, genre_id ) VALUES ('{newMovieId}', '{genreID1}')")
        db = pyodbc.connect(conn_str)
        cur = db.cursor()
        cur.execute(query2)
        cur.commit()
    if genreID2 in genre_list:
        query3 = (f"INSERT INTO MovieGenre (movie_id, genre_id ) VALUES ('{newMovieId}', '{genreID2}')")
        db = pyodbc.connect(conn_str)
        cur = db.cursor()
        cur.execute(query3)
        cur.commit()
    if genreID3 in genre_list:
        query4 = (f"INSERT INTO MovieGenre (movie_id, genre_id ) VALUES ('{newMovieId}', '{genreID3}')")
        db = pyodbc.connect(conn_str)
        cur = db.cursor()
        cur.execute(query4)
        cur.commit()
def AddPredeccor(movie_id, predeccors_id):
    query = (f"INSERT INTO MoviePredeccors (movie_id, predeccors_id ) VALUES ('{movie_id}', '{predeccors_id}')")
    db = pyodbc.connect(conn_str)
    cur = db.cursor()
    cur.execute(query)
    cur.commit()
def AddMovieSession(movie_id,theatre_id,slot,date):
    query = (f"SELECT TOP 1 * FROM Sessions ORDER BY session_id DESC")
    lastSession = query_db(query)
    lastSessionId = lastSession[0]['session_id']
    newSessionId = lastSessionId + 1
    query = (f"INSERT INTO Sessions (session_id, movie_id ) VALUES ('{newSessionId}', '{movie_id}')")
    db = pyodbc.connect(conn_str)
    cur = db.cursor()
    cur.execute(query)
    cur.commit()
    query = (f"INSERT INTO TheatreSessions (session_id, theatre_id, time_slot,date ) VALUES ('{newSessionId}', '{theatre_id}', '{slot}', '{date}')")
    db = pyodbc.connect(conn_str)
    cur = db.cursor()
    cur.execute(query)
    cur.commit()





        
