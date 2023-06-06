from django.shortcuts import render,redirect
from django.http import HttpResponse
from Project2_app.users.login import *
from Project2_app.users.forms import *
from Project2_app.users.shows import *

def loginIndex(request):
    context = {"login_fail": False, "login_form":LoginForm()}    
    return render(request, 'Project2_app/login.html', context)

def login(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    loginCheck = checkCreditentials(username, password)
    isDataBaseManager = CheckUserDatabaseManager(username,password)
    if(isDataBaseManager):
        request.session['username'] = username
        return redirect('../databasemanager/')
    if(loginCheck):
        request.session['username'] = username
        if(CheckUserDirector(username)):
          return redirect('../director/')  
        if(CheckUserAudience(username)):
          return redirect('../audience/')
    context = {"login_fail": True, "login_form":LoginForm()}    
    return render(request, 'Project2_app/login.html', context)

def home(request):
    if('username' in request.session):
        username = request.session['username']
    else: 
        return redirect('../login/')
    username = request.session['username']
    if(username == None):
        return redirect('../login/')
    return render(request, 'Project2_app/home.html', {"username":username})

def databasemanager(request):
    if('username' in request.session):
        username = request.session['username']
    else: 
        return redirect('../login/')
    username = request.session['username']
    if(username == None):
        return redirect('../login/')
    # users = GetUsers()
    directors = GetDirectors()
    return render(request, 'Project2_app/databasemanager.html', {"username":username } )

def databasemanagerAudiences(request):
    if('username' in request.session):
        username = request.session['username']
    else: 
        return redirect('../login/')
    audiences = GetAudiences()
    return render(request, 'Project2_app/databasemanageraudiences.html', {"username":username , "audiences" : audiences, "add_audience_form" : AddAudienceForm(),"delete_audience_form" : DeleteAudienceForm(), "show_movies_audience_form": ShowMoviesOfAudiencefrom()} )

def databasemanagerAddAudience(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    name = request.POST.get("name")
    surname = request.POST.get("surname")
    print("Will be adding user : " ,username,password,name,surname)
    AddUser(username,password,name,surname)
    AddAudience(username)
    audiences = GetAudiences()
    print("Added user : " ,username,password,name,surname)
    return redirect('databasemanagerAudiences')
    # return render(request, 'Project2_app/databasemanageraudiences.html', {"username":username , "audiences" : audiences, "add_audience_form" : AddAudienceForm(),"delete_audience_form" : DeleteAudienceForm()} )

def databasemanagerDeleteAudience(request):
    username = request.POST.get("username")
    DeleteUser(username)
    print("Deleted username : ", username)
    return redirect('databasemanagerAudiences')

def databasemanagerAudienceMovies(request):
    if('username' in request.session):
        username = request.session['username']
    else: 
        return redirect('../login/')
    username = request.POST.get("username")
    movies = GetAudienceMovies(username)
    print("Buraya geldik")
    return render(request, 'Project2_app/databasemanageraudiencemovies.html', {"username":username , "movies": movies} )

def databasemanagerDirectors(request):
    if('username' in request.session):
        username = request.session['username']
    else: 
        return redirect('../login/')
    directors = GetDirectors()
    platforms = GetPlatforms()
    return render(request, 'Project2_app/databasemanagerdirectors.html', {"username":username , "directors": directors,"platforms" : platforms, "add_director_form" : AddDirectorForm(),"update_director_form" : UpdateDirectorForm(),"delete_director_form" : DeleteDirectorForm(), "show_movies_director_form":ShowMoviesOfDirectorForm} )
def databasemanagerAddDirector(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    name = request.POST.get("name")
    surname = request.POST.get("surname")
    nation = request.POST.get("nation")
    platform_id = request.POST.get("platform")
    AddUser(username,password,name,surname)
    AddDirector(username,nation,platform_id)
    return redirect('databasemanagerDirectors')

def databasemanagerUpdateDirector(request):
    director_username = request.POST.get("username")
    platform_id = request.POST.get("platform")
    UpdateDirector(director_username,platform_id)
    return redirect('databasemanagerDirectors')

def databasemanagerDirectorMovies(request):
    director_username = request.POST.get("username")
    directormovies = GetDirectorMovieSessions(director_username)
    return render(request, 'Project2_app/databasemanagerdirectormovies.html', {"username":director_username , "directormovies": directormovies} )

def databasemanagerDeleteDirector(request):

    return redirect('databasemanagerDirectors')

def databaseManagerMovies(request):
    if('username' in request.session):
        username = request.session['username']
    else: 
        return redirect('../login/')
    moviesWithRate = GetMoviesWithRate()
    return render(request, 'Project2_app/databasemanagermovies.html', {"username":username , "moviesWithRate": moviesWithRate} )



def director(request):
    if('username' in request.session):
        username = request.session['username']
    else: 
        return redirect('../login/')
    username = request.session['username']
    if(username == None):
        return redirect('../login/')
    director =  GetDirectorInformation(username)
    directorMovies = GetDirectorMoviesWithGenre(username)
    directorMovieSessions = GetDirectorMovieSessions(username)
    theatres = GetTheatres()
    return render(request, 'Project2_app/director.html', {"username":username, "director":director, "directorMovies": directorMovies, "directorMovieSessions" : directorMovieSessions,"theatres": theatres, "add_movie_form" : AddMovieForm() , "add_predeccor_form" : AddPredeccorsForm(), "add_movie_session_form": AddMovieSessionForm()})

def directorAddMovie(request):
    username = request.session['username']
    movieName = request.POST.get("movieName")
    duration = request.POST.get("duration")
    genreID = request.POST.get("genreID")
    genreID1 = request.POST.get("genreID1")
    genreID2 = request.POST.get("genreID2")
    genreID3 = request.POST.get("genreID3")
    AddMovie(username,movieName,duration,genreID,genreID1,genreID2,genreID3)
    return redirect('director')
def directorAddPredeccor(request):
    movie_id = request.POST.get("movieID")
    predeccors_id= request.POST.get("predeccorID")
    AddPredeccor(movie_id, predeccors_id)
    return redirect('director')
def directorAddMovieSession(request):
    movie_id = request.POST.get("movieId")
    theatre_id = request.POST.get("theatreId")
    slot = request.POST.get("slot")
    date = request.POST.get("date")
    print("Date :" , date)
    AddMovieSession(movie_id,theatre_id,slot,date)

    return redirect('director')


def audience(request):
    if('username' in request.session):
        username = request.session['username']
    else: 
        return redirect('../login/')
    username = request.session['username']
    if(username == None):
        return redirect('../login/')
    audiencePlatforms = GetAudiencePlatforms(username)
    platformSessions = GetAudiencePlatformSessions(username)
    otherPlatformSessions = GetOtherPlatformSessions(username)
    boughtMovieSessions = GetBoughtMovieSessions(username)
    watchedMovieSessions = GetWatchedMovieSessions(username)
    return render(request, 'Project2_app/audience.html', {"username":username, "audiencePlatforms" : audiencePlatforms, "platformSessions" : platformSessions, "boughtMovieSessions": boughtMovieSessions, "otherPlatformSessions":otherPlatformSessions,"watchedMovieSessions": watchedMovieSessions ,"add_audience_platform_form": AddAudiencePlatformForm(), "add_audience_session_form" : AddAudienceSessionForm(), "add_movie_rating_form": AddMovieRatingForm() })

def audienceAddPlatform(request):
    username = request.session['username']
    platform_id = request.POST.get("platformId")
    AddPlatformToAudience(username,platform_id)
    return redirect('audience')
def audienceAddSession(request):
    username = request.session['username']
    session_id = request.POST.get("sessionId")
    AddAudienceSession(username,session_id)
    return redirect('audience')

def audienceAddMovieRating(request):
    username = request.session['username']
    movie_id = request.POST.get("movieId")
    rate = request.POST.get("rate")
    AddMovieRating(username, movie_id,rate)
    return redirect('audience')
