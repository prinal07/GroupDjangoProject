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

    # list of accomodations for the dropdown select tag
    accommodation = forms.ChoiceField(choices=[('none', 'Select an option'),
                                        ('Other', 'Other'),
                                        ('Birks Grange Village', 'Birks Grange Village'),
                                        ('Clydesdale Court', 'Clydesdale Court'),
                                        ('Cook & Llewellyn Mews', 'Cook & Llewellyn Mews'),
                                        ('Duryard', 'Duryard'),
                                        ('East Park', 'East Park'),
                                        ('Garden Hill House', 'Garden Hill House'),
                                        ('Holland Hall Studios', 'Holland Hall Studios'),
                                        ('James Owen Court', 'James Owen Court'),
                                        ('King Edward Court', 'King Edward Court'),
                                        ('Lafrowda', 'Lafrowda'),
                                        ('Moberly', 'Moberly'),
                                        ('Nacherrow', 'Nacherrow'),
                                        ('Nash Grove', 'Nash Grove'),
                                        ('Rowancroft', 'Rowancroft'),
                                        ('Rowe House', 'Rowe House'),
                                        ('Spreytonway', 'Spreytonway'),
                                        ('St Germans', 'St Germans'),
                                        ('St Davids', 'St Davids'),
                                        ('Exeter Halls', 'Exeter Halls'),
                                        ('Holland Hall', 'Holland Hall'),
                                        ('Mardon Hall', 'Mardon Hall')], required=True,label='Accommodation')
    

    # Replaces the template information in UserCreationForm
    class Meta:
        # Reflects the form to input data to populate an empty User model
        model = User
        # Field identifiers to retrieve data from a POST request
        fields = ['username','email','accommodation','password1','password2']