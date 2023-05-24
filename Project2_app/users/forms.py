from django import forms

class LoginForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    surname = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Surname'}))