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