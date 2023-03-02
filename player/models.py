from django.db import models


# Created a model here.

class Fact(models.Model):
    date = models.DateField()
    fact = models.TextField()

    def __str__(self):
        return f"{self.date} - {self.fact}"


class Bin(models.Model):
    bin_number = models.IntegerField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    poi_info = models.TextField(max_length=30)

    def __str__(self):
        return f'{self.latitude}, {self.longitude}'
