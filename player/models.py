from django.db import models

# Create your models here.

class Fact(models.Model):
    date = models.DateField()
    fact = models.TextField()

    def __str__(self):
        return f"{self.date} - {self.fact}"
