from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.validators import RegexValidator



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

class Suspect(models.Model):
    story = models.ForeignKey('Story', on_delete=models.CASCADE, related_name='suspects', default=0)
    number = models.IntegerField(default=1)
    name = models.TextField(max_length=30, default="")
    brief = models.TextField(max_length=500, default="")
    
    class Meta:
        ordering = ['number']
    
    def save(self, *args, **kwargs):
        if not self.pk:  # if this is a new object being saved
            # get the maximum number currently in the database and increment it by 1
            self.number = self.story.suspects.count() + 1
        super().save(*args, **kwargs)


class Story(models.Model):
    MAX_SUSPECTS = 5
    
    story_number = models.IntegerField(default=1)

    sprite_1 = models.CharField(max_length=1, validators=[RegexValidator(r'^[0-9]+$')])
    sprite_2 = models.CharField(max_length=1, validators=[RegexValidator(r'^[0-9]+$')])
    sprite_3 = models.CharField(max_length=1, validators=[RegexValidator(r'^[0-9]+$')])
    sprite_4 = models.CharField(max_length=1, validators=[RegexValidator(r'^[0-9]+$')])
    sprite_5 = models.CharField(max_length=1, validators=[RegexValidator(r'^[0-9]+$')])

    sprite_codes = str(sprite_1) + str(sprite_2) + str(sprite_3) + str(sprite_4) + str(sprite_5)

    clue1 = models.TextField(max_length=400, default="")
    clue2 = models.TextField(max_length=400, default="")
    clue3 = models.TextField(max_length=400, default="")
    clue4 = models.TextField(max_length=400, default="")
    clue5 = models.TextField(max_length=400, default="")
    clue6 = models.TextField(max_length=400, default="")
    clue7 = models.TextField(max_length=400, default="")
    clue8 = models.TextField(max_length=400, default="")
    clue9 = models.TextField(max_length=400, default="")
    clue10 = models.TextField(max_length=400, default="")
    
    clues = [clue1, clue2, clue3, clue4, clue5, clue6, clue7, clue8, clue9, clue10]
    
    culprit = models.CharField(max_length=1, validators=[RegexValidator(r'^[0-9]$')])
    
    def can_add_suspect(self):
        return self.suspects.count() < self.MAX_SUSPECTS

    def __str__(self):
        return f'Story {self.story_number}'    
    
    def get_suspects(self):
        return self.suspect_set.all()
    
    def get_description(self):
        return [suspect.brief for suspect in self.get_suspects()]
    
    def getCulprit(self):
        return self.culprit
    
    def getSpritesCodes(self):
        return self.sprite_codes
    
    def getAllClues(self):
        return self.clues
    




