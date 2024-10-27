from django import forms
from .models import User
from django.contrib.auth.forms import AuthenticationForm


# Login form for custom authentication
class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=250,
                               required=True,
                               label='username/phone number',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))

    password = forms.CharField(max_length=250,
                               required=True,
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))
