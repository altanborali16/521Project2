from django.shortcuts import render,redirect
from django.http import HttpResponse
from Project2_app.users.login import *
from Project2_app.users.forms import *
from Project2_app.users.shows import *
# Create your views here.

def index(request):
    index_text = "view.index is called"
    context = {'index_text': index_text}
    return render(request, 'renders/index.html',context)

def printNumber(request,number):
    numbers = [i for i in range(number,number+5)]
    arr = []
    for i in range(len(numbers)):
        arr.append({"index": i, "number": numbers[i]})
    return render(request,'renders/numbers.html',{"arr": arr})

def printString(request,string):
    t = string + "321"
    return HttpResponse(f'view.printString function is called with string given: {string}, and added \"321\" is: {t}')

def loginIndex(request):
    context = {"login_fail": False, "login_form":LoginForm()}    
    return render(request, 'Project2_app/login.html', context)

def login(request):
    name = request.POST.get("name")
    surname = request.POST.get("surname")
    loginCheck = checkCreditentials(name, surname)
    if(loginCheck):
        request.session['name'] = name
        return redirect('../home/')
    context = {"login_fail": True, "login_form":LoginForm()}    
    return render(request, 'Project2_app/login.html', context)

def home(request):
    if('name' in request.session):
        name = request.session['name']
    else: 
        return redirect('../login/')
    name = request.session['name']
    if(name == None):
        return redirect('../login/')
    return render(request, 'Project2_app/home.html', {"name":name})

def listShows(request, genre):
    if('name' in request.session):
        name = request.session['name']
    else: 
        return redirect('../login/')
    if(name == None):
        return redirect('../login/')
    shows =[]
    genreTitle = ""
    if(genre == 0): #mystery
        shows = returnMysteryActionShows(name)
        genreTitle = "Mystery/Action"
    elif(genre == 1): #distopian
        shows = returnDramaDistopianShows(name)
        genreTitle = "Drama/Distopian"
    elif(genre == 2): #comedy
        shows = returnComedyShows(name)
        genreTitle = "Comedy"
    elif genre == 3:
        shows = returnPopularShows()
    else:
        return redirect('../home')
    if(len(shows) == 0):
        shows = False
    return render(request, 'Project2_app/shows.html', {"name": name, "shows": shows, "genre":genreTitle})