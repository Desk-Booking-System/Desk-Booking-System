from django import forms
from .MODELS.models import Desk

class LoginForm(forms.Form):
    username = forms.CharField()   
    password = forms.CharField(widget = forms.PasswordInput)


class DeskForm(forms.Form):
    # id = forms.CharField(widget=forms.I)
    date = forms.DateField(widget=forms.DateInput(attrs={'type':'date' }))