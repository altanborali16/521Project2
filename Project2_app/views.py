from django.shortcuts import render
from django.http import HttpResponse
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