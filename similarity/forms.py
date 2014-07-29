from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from models import *



class UserForm(UserChangeForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "image", "username", "password")

