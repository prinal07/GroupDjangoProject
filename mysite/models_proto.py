from django.db import models

class User(models.Model):
    profileType = models.IntegerField(default=2) # 2 for user, 1 for game-keeper, 0 for developer
    fname = models.CharField(max_length = 20)
    lname = models.CharField(max_length = 20)
    email = models.CharField(max_length = 50)
    username = models.CharField(max_length = 20)
    password = models.CharField(max_length = 30)
    userType = models.IntegerField(default=0) # 0 for student, 1 for staff
    group = models.IntegerField(default = 0) # 0 for global group?
    level = models.IntegerField(default = 0) 
    points = models.IntegerField(default = 0)
    profilePicture = models.IntegerField(default = 0)

class Group(models.Model):
    groupName = models.CharField(max_length = 30)
    isDepartment = models.BooleanField(default = False)
    isAccomodation = models.BooleanField(default = False)

class Challenge(models.Model):
    challengeText = models.CharField(max_length = 200)
