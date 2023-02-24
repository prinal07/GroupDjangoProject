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

    def __str__(self):
        return self.username
