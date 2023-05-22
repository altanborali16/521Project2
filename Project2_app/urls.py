from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('<int:number>', views.printNumber, name='printNumber'),
    path('<str:string>', views.printString, name='printString'),
]