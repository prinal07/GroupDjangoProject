from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db import models


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    accommodation = forms.CharField(required=True,label='Accommodation')

    class Meta:
        model = User
        fields = ['username','email','accommodation','password1','password2']
