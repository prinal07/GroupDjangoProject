from datetime import date

import math
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# Store user information
class Account(models.Model):
    profileClass = models.IntegerField(default=0)
    accommodation = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    group = models.IntegerField(default=0)
    level = models.IntegerField(default=0)
    points = models.IntegerField(default=0)
    daily_points = models.IntegerField(default=0)
    last_day_accessed = models.DateField(default=date.today)
    staffCheck = models.BooleanField(default=False)

    def current_level(self):
        return math.ceil(self.points / 100)

    def level_progress(self):
        return self.points % 100

    def is_my_bool_field_true(self):
        if self.staffCheck:
            return "Yes"
        else:
            return "No"

    is_my_bool_field_true.short_description = "University Staff"

    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username}Profile'
