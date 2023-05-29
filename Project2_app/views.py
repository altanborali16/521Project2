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
    if(len(request.POST) == 5):
        databasemanagerAddAudience(request)
    if(len(request.POST) == 2):
        databasemanagerDeleteAudience(request)
    print("Buraya giriyor mu")
    if('username' in request.session):
        username = request.session['username']
    else: 
        return redirect('../login/')
    username = request.session['username']
    if(username == None):
        return redirect('../login/')
    users = GetUsers()
    directors = GetDirectors()
    return render(request, 'Project2_app/databasemanager.html', {"username":username , "users" : users, "directors": directors, "add_audience_form" : AddAudienceForm(),"delete_audience_form" : DeleteAudienceForm()} )

def databasemanagerAddAudience(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    name = request.POST.get("name")
    surname = request.POST.get("surname")
    print("Will be adding user : " ,username,password,name,surname)
    AddUser(username,password,name,surname)
    AddAudience(username)
    print("Added user : " ,username,password,name,surname)

def databasemanagerDeleteAudience(request):
    username = request.POST.get("username")
    DeleteUser(username)
    print("Deleted username : ", username)

def director(request):
    if('username' in request.session):
        username = request.session['username']
    else: 
        return redirect('../login/')
    username = request.session['username']
    if(username == None):
        return redirect('../login/')
    return render(request, 'Project2_app/director.html', {"username":username})


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