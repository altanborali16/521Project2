from django.urls import path
from . import views

urlpatterns = [
    # path('',views.index, name='index'),
    # path('<int:number>', views.printNumber, name='printNumber'),
    # path('<str:string>', views.printString, name='printString'),
    path('', views.loginIndex, name='loginIndex'),
    path('login/', views.loginIndex, name='loginIndex'),
    path('login/#', views.login, name='login'),

    path('databasemanager/', views.databasemanager, name='databasemanager'),

    path('databasemanager/audiences', views.databasemanagerAudiences, name='databasemanagerAudiences'),
    path('databasemanager/addaudience', views.databasemanagerAddAudience, name='databasemanagerAddAudience'),
    path('databasemanager/deleteaudience', views.databasemanagerDeleteAudience, name='databasemanagerDeleteAudience'),
    path('databasemanager/audiencemovies', views.databasemanagerAudienceMovies, name='databasemanagerAudienceMovies'),

    path('databasemanager/directors', views.databasemanagerDirectors, name='databasemanagerDirectors'),
    path('databasemanager/addDirector', views.databasemanagerAddDirector, name='databasemanagerAddDirector'),
    path('databasemanager/updateDirector', views.databasemanagerUpdateDirector, name='databasemanagerUpdateDirector'),
    path('databasemanager/directorMovies', views.databasemanagerDirectorMovies, name='databasemanagerDirectorMovies'),
    path('databasemanager/deleteDirector', views.databasemanagerDeleteDirector, name='databasemanagerDeleteDirector'),

    path('databasemanager/movies', views.databaseManagerMovies, name='databaseManagerMovies'),

    # path('databasemanager/', views.databasemanagerAddAudience, name='AddAudience'),
    # path('databasemanager/', views.databasemanagerDeleteAudience, name='DeleteAudience'),

    path('director/', views.director, name='director'),
    path('director/addMovie', views.directorAddMovie, name='directorAddMovie'),
    path('director/addPredeccor', views.directorAddPredeccor, name='directorAddPredeccor'),
    path('director/addMovieSession', views.directorAddMovieSession, name='directorAddMovieSession'),

    path('audience/', views.audience, name='audience'),
    path('audience/addPlatform', views.audienceAddPlatform, name='audienceAddPlatform'),
    path('audience/addAudienceSession', views.audienceAddSession, name='audienceAddSession'),
    path('audience/addMovieRating', views.audienceAddMovieRating, name='audienceAddMovieRating'),


]