from django.urls import path
from . import views

urlpatterns = [
    # path('',views.index, name='index'),
    # path('<int:number>', views.printNumber, name='printNumber'),
    # path('<str:string>', views.printString, name='printString'),
    path('', views.loginIndex, name='loginIndex'),
    path('login/', views.loginIndex, name='loginIndex'),
    path('login/#', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('databasemanager/', views.databasemanager, name='databasemanager'),
    # path('databasemanager/', views.databasemanagerAddAudience, name='AddAudience'),
    # path('databasemanager/', views.databasemanagerDeleteAudience, name='DeleteAudience'),
    path('director/', views.director, name='director'),
    # path('shows/<int:genre>', views.listShows, name='listshows'),
]