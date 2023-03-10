from datetime import date

import math
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# Store user information
class Account(models.Model):
    """Account model used by Django to populate the db.sqlite3 database, and store information of individual users

    Args:
        models.Model (super): A built-in Django model structure, that is adapted by this Class

    Methods:
        current_level(): Returns the current level of the user
        level_progress(): Returns the percentage progress to the next level (every 100 points)
        is_my_bool_field_true(): Returns the boolean if the user is Staff
        __str__(): Represents the model as a string in a specfied format
        account_dailypoints(): Returns the number of points achieved by the account today
        account_points(): Returns the number of points achieved in total
    """
    
    # Model Fields, to be populated and used within the database. Using Django model types to collect preferred data
    # type information from the user
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

    def current_level(self):
        """Returns the level of an individual account

        Returns:
            int: To reflect 100 points a level, division and round up, Levels possible == [1..]
        """
        return math.ceil(self.points / 100) 

    def level_progress(self):
        """Returns the percentage of progress to the next level of an individual account

        Returns:
            int: The remainder of the current points to the next 100 (level threshold)
        """
        return self.points % 100

    ######################################## TODO: Rename the function throughout the code base to make sense:
    ######################################## is_account_staff perhaps
    def is_my_bool_field_true(self):
        """Determine if the Account is designated as a staff or student

        Returns:
            string: String boolean representation, "Yes"/"No", to represent
        """
        if self.staffCheck:
            return "Yes"
        else:
            return "No"

    # Provide a description of the functions purpose to be represented when in use
    is_my_bool_field_true.short_description = "University Staff"

    def __str__(self):
        """Chosen string representation format of an individual model

        Returns:
            string: The model username
        """
        return self.username
    
    def account_dailypoints(self):
        """Return the amount of points received today by an individual account

        Returns:
            int: The amount of points received today
        """
        return self.daily_points
    
        
    def account_points(self):
        """Return the total number of points owned by an individual account

        Returns:
            int: The number of points achieved
        """
        return self.points


class Profile(models.Model):
    """Profile model, to store information related to a User for use in representation

    Args:
        models.Model (super): Django's built in Model structure, to be adapted by the attributes of this class
    
    Methods:
        __str__(): String Representation of the Model Function
    
    """
    
    # Attributes (Columns) of the Model
    # Foreign Key of an existing User Model stored in the table
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    # Picture that can be submitted to the database in User Creation
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        """Chosen string representation format of an individual model

        Returns:
            string: The Username of the user attribute foreign key
        """
        return f'{self.user.username}Profile'
