from django.db import models

# Create your models here.

class User(models.Model):
    profileClass = models.IntegerField(default = 0)
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    email = models.CharField(max_length = 30)
    username = models.CharField(max_length = 20)
    password = models.CharField(max_length = 20)
    group = models.IntegerField(default = 0)
    level = models.IntegerField(default = 0)
    points = models.IntegerField(default = 0)

class Group(models.Model):
    groupName = models.CharField(max_length = 30)
    points = models.IntegerField(default = 0)
    isDepartment = models.BooleanField()
    isAccomodation = models.BooleanField()

class Challenge(models.Model):
    challengeText = models.CharField(max_length = 200)
