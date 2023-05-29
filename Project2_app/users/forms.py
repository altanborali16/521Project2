from django import forms

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