from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db import models


class UserRegistrationForm(UserCreationForm):
    """Generates the items required for display and interaction in the User Registration process.

    Args:
        UserCreationForm (super): A built-in django form structure, that is adapted within this class
    """
    
    # Defines special fields to be placed in the form, and their field type
    email = forms.EmailField()
    accommodation = forms.CharField(required=True,label='Accommodation')

    # Replaces the template information in UserCreationForm
    class Meta:
        # Reflects the form to input data to populate an empty User model
        model = User
        
        # Field identifiers to retrieve data from a POST request
        fields = ['username','email','accommodation','password1','password2']
