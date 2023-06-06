from django import forms
from Project2_app.dbConnection import *

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Password'}))

class AddAudienceForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}),required=True)
    password = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Password'}),required=True)
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name'}),required=True)
    surname = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Surname'}),required=True)
class DeleteAudienceForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}),required=True)

class ShowMoviesOfAudiencefrom(forms.Form):
    # audiences = GetAudiences()
    # print(audiences)
    # user_choices = [(user['username'], user['username']) for user in audiences]
    # username = forms.ChoiceField(choices=user_choices)
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}),required=True)
    # username = forms.CharField(widget=forms.Select(choices=[(choice['username'], choice['username']) for choice in audiences]), required=True)

class AddDirectorForm(forms.Form):
    nations = GetNations()
    # print("form : " , nations)
    platforms = GetPlatforms()
    # print("form : ", platforms)
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}),required=True)
    password = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Password'}),required=True)
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name'}),required=True)
    surname = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Surname'}),required=True)
    nation = forms.CharField(widget=forms.Select(choices=[(choice['nation'], choice['nation']) for choice in nations]), required=True)
    platform = forms.CharField(widget=forms.Select(choices=[(choice['platform_id'], choice['platform_id']) for choice in platforms]), required=True)
    # platform = forms.ModelChoiceField(queryset=GetPlatforms(),empty_label='Select a platform',required=True)
class UpdateDirectorForm(forms.Form):
    platforms = GetPlatforms()
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}),required=True)
    platform = forms.CharField(widget=forms.Select(choices=[(choice['platform_id'], choice['platform_id']) for choice in platforms]), required=True)
class ShowMoviesOfDirectorForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}),required=True)

class DeleteDirectorForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}),required=True)

class AddMovieForm(forms.Form):
    # movieId = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Movie Id'}),required=True)
    movieName = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Movie Name'}),required=True)
    duration = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Duration'}), required=True)
    genreID = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Genre Id'}), required=True)
    genreID1 = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Genre Id Additional'}),required=False)
    genreID2 = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Genre Id Additional'}),required=False)
    genreID3 = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Genre Id Additional'}),required=False)

class AddPredeccorsForm(forms.Form):
    movieID = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Movie Id'}), required=True)
    predeccorID = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Predeccor Id'}), required=True)

class AddMovieSessionForm(forms.Form):
    movieId = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Movie Id'}), required=True)
    theatreId = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Theatre Id'}), required=True)
    slot = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Slot'}), required=True)
    date = forms.DateField(widget=forms.DateInput(attrs={'placeholder': 'YYYY/MM/DD'}), required=True)

class AddAudiencePlatformForm(forms.Form):
    platformId = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Platform Id'}), required=True)

class AddAudienceSessionForm(forms.Form):
    sessionId = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Session Id'}), required=True)

class AddMovieRatingForm(forms.Form):
    movieId = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Movie Id'}), required=True)
    rate = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Rate'}), required=True)