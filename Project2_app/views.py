from django.shortcuts import render,redirect
from django.http import HttpResponse
from Project2_app.users.login import *
from Project2_app.users.forms import *
from Project2_app.users.shows import *
# Create your views here.

# def index(request):
#     index_text = "view.index is called"
#     context = {'index_text': index_text}
#     return render(request, 'renders/index.html',context)

# def printNumber(request,number):
#     numbers = [i for i in range(number,number+5)]
#     arr = []
#     for i in range(len(numbers)):
#         arr.append({"index": i, "number": numbers[i]})
#     return render(request,'renders/numbers.html',{"arr": arr})

# def printString(request,string):
#     t = string + "321"
#     return HttpResponse(f'view.printString function is called with string given: {string}, and added \"321\" is: {t}')

def loginIndex(request):
    context = {"login_fail": False, "login_form":LoginForm()}    
    return render(request, 'Project2_app/login.html', context)

def login(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    loginCheck = checkCreditentials(username, password)
    isDataBaseManager = CheckUserDatabaseManager(username,password)
    if(loginCheck):
        request.session['username'] = username
        if(CheckUserDirector(username)):
          return redirect('../director/')  
        return redirect('../home/')
    if(isDataBaseManager):
            request.session['username'] = username
            return redirect('../databasemanager/')
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
    # if(len(request.POST) == 5):
    #     databasemanagerAddAudience(request)
    # if(len(request.POST) == 2):
    #     databasemanagerDeleteAudience(request)
    # print("Buraya giriyor mu")
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




# def listShows(request, genre):
#     if('name' in request.session):
#         name = request.session['name']
#     else: 
#         return redirect('../login/')
#     if(name == None):
#         return redirect('../login/')
#     shows =[]
#     genreTitle = ""
#     if(genre == 0): #mystery
#         shows = returnMysteryActionShows(name)
#         genreTitle = "Mystery/Action"
#     elif(genre == 1): #distopian
#         shows = returnDramaDistopianShows(name)
#         genreTitle = "Drama/Distopian"
#     elif(genre == 2): #comedy
#         shows = returnComedyShows(name)
#         genreTitle = "Comedy"
#     elif genre == 3:
#         shows = returnPopularShows()
#     else:
#         return redirect('../home')
#     if(len(shows) == 0):
#         shows = False
#     return render(request, 'Project2_app/shows.html', {"name": name, "shows": shows, "genre":genreTitle})