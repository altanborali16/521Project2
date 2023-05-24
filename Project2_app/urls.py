from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('<int:number>', views.printNumber, name='printNumber'),
    path('<str:string>', views.printString, name='printString'),

    path('login/', views.loginIndex, name='loginIndex'),
    path('login/#', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('shows/<int:genre>', views.listShows, name='listshows'),
]