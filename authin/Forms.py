from django import forms
from django.forms import ModelForm
from .models import user_a
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignInForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name','last_name','email','password1', 'password2']

class LoginForm(ModelForm):
    class Meta:
        model = user_a
        fields = ['user_name', 'pass_word']
        