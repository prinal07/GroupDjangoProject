from datetime import date

import math
from django.db import models
from django.contrib.auth.models import User
from game.models import Challenge


# Store user information
class Account(models.Model):
    """
    A class representing the Account of a registered and authenticated user. 

    Attributes:
    ------------ 
    profileClass : int 
        Profile class of the user.
    accommodation : str 
        Accommodation the user is staying at.
    email : str 
        Email address of the user.
    username : str 
        Username of the user whose account this represents.
    password : str 
        Password of the corresponding user.
    group : int 
        The group of the account.
    level : int 
        The current level of the user's account
    points : int
        Total points earned by the account.
    daily_points : int
        Daily points earned by the account.
    last_day_accessed : date
        Last day the account was accessed.
    staffCheck : bool
        Check whether the user is a student or a university staff member.
    challenges : ManyToMany Relationship
        Many to many relationship between Account and Challenge

    Methods:
    --------- 
    current_level(): 
        Returns the current level of the account based on the points earned.
    level_progress(): 
        Returns the progress towards the next level based on the points earned.
    is_my_bool_field_true(): 
        Checks whether the staffCheck field is True or False and returns "Yes" or "No" accordingly. Used to display the same in the admin.py file.
    __str__(): 
        Returns the username of the account.
    account_dailypoints(): 
        Returns the daily points of the account.
    account_points(): 
        Returns the total points of the account.
        
    """
    profileClass = models.IntegerField(default=0)
    accommodation = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    group = models.IntegerField(default=0)
    level = models.IntegerField(default=1)
    points = models.IntegerField(default=0)
    daily_points = models.IntegerField(default=0)
    last_day_accessed = models.DateField(default=date.today)
    staffCheck = models.BooleanField(default=False)
    challenges = models.ManyToManyField(Challenge, related_name='accounts')


    def current_level(self):
        """
        Returns the current level of the account based on the points earned.
        """
        return math.ceil(self.points / 100)

    def level_progress(self):
        """
        Returns the progress towards the next level based on the points earned.
        """
        return self.points % 100

    def is_my_bool_field_true(self):
        """
        Checks whether the staffCheck field is True or False and returns "Yes" or "No" accordingly. Used to display the same in the admin.py file.
        """
        if self.staffCheck:
            return "Yes"
        else:
            return "No"

    is_my_bool_field_true.short_description = "University Staff"

    def __str__(self):
        """
        Returns the username of the account.
        """
        return self.username
    
    def account_dailypoints(self):
        """
        Returns the daily points of the account.
        """
        return self.daily_points
    
        
    def account_points(self):
        """
        Returns the total points of the account.
        """
        return self.points


class Profile(models.Model):
    """
    A class representing a user profile.

    Attributes:
    ------------ 
    user : User
        A one-to-one relationship with the User object.
    image : ImageField
        An image field that stores the profile picture of the user.
        If no image is uploaded, the default image 'default.jpg' will be used.
        The images will be uploaded to a directory named 'profile_pics'.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        """
        Returns the username of the associated user followed by 'Profile'.
        """
        return f'{self.user.username}Profile'
