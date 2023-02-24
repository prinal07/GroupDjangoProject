from django.db import models


# Create your models here.

# Store user information
class User(models.Model):
    profileClass = models.IntegerField(default=0)
    accommodation = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    group = models.IntegerField(default=0)
    level = models.IntegerField(default=0)
    points = models.IntegerField(default=0)
    staffCheck = models.BooleanField()


    def is_my_bool_field_true(self):
        if self.staffCheck:
            return "Yes"
        else:
            return "No"

    is_my_bool_field_true.short_description = "University Staff"
        
    def __str__(self):
        return self.username


class Group(models.Model):
    groupName = models.CharField(max_length = 30)
    points = models.IntegerField(default = 0)
    isDepartment = models.BooleanField()
    isAccomodation = models.BooleanField()

    def __str__(self):
        return self.groupName

# class Challenge(models.Model):
#     challengeTitle = models.CharField(max_length = 50)
#     challengeText = models.CharField(max_length = 200)

#     def __str__(self):
#         return self.challengeTitle
 
class Accomodation(models.Model):
    accomodationName = models.CharField(max_length = 30)

    def __str__(self):
        return self.accomodationName

class Department(models.Model):
    departmentName = models.CharField(max_length = 30)
    
    def __str(self):
        return self.departmentName
