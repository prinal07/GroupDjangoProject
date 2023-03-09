from django.db import models
from django.db.models import Max, Q


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




#     MAX_SUSPECTS = 5
    
#     def limit_suspect_choices():
#         return Q(story_suspect1__isnull=True) | \
#                Q(story_suspect2__isnull=True) | \
#                Q(story_suspect3__isnull=True) | \
#                Q(story_suspect4__isnull=True) | \
#                Q(story_suspect5__isnull=True)
    
#     suspect1 = models.ForeignKey(Suspect, on_delete=models.CASCADE, related_name='story_suspect1')
#     suspect2 = models.ForeignKey(Suspect, on_delete=models.CASCADE, related_name='story_suspect2', blank=True, null=True)
#     suspect3 = models.ForeignKey(Suspect, on_delete=models.CASCADE, related_name='story_suspect3', blank=True, null=True)
#     suspect4 = models.ForeignKey(Suspect, on_delete=models.CASCADE, related_name='story_suspect4', blank=True, null=True)
#     suspect5 = models.ForeignKey(Suspect, on_delete=models.CASCADE, related_name='story_suspect5', blank=True, null=True)

#     suspects = [suspect1, suspect2, suspect3, suspect4, suspect5]

#     spriteCodes = models.TextField(max_length=5)


#     description = [suspect1.brief, suspect2.brief, suspect3.brief, suspect4.brief, suspect5.brief]
    
#     clue1 = models.TextField(max_length=100, default="")
#     clue2 = models.TextField(max_length=100, default="")
#     clue3 = models.TextField(max_length=100, default="")
#     clue4 = models.TextField(max_length=100, default="")
#     clue5 = models.TextField(max_length=100, default="")
#     clue6 = models.TextField(max_length=100, default="")
#     clue7 = models.TextField(max_length=100, default="")
#     clue8 = models.TextField(max_length=100, default="")
#     clue9 = models.TextField(max_length=100, default="")
#     clue10 = models.TextField(max_length=100, default="")

#     clues = [clue1, clue2, clue3, clue4, clue5, clue6, clue7, clue8, clue9, clue10]
#     culprit = models.CharField(max_length=1)

class Story(models.Model):
    MAX_SUSPECTS = 5
    
    story_number = models.IntegerField(default=1)
    sprite_codes = models.TextField(max_length=5, default="")
    
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
    
    culprit = models.CharField(max_length=1, default='')
    
    def can_add_suspect(self):
        return self.suspects.count() < self.MAX_SUSPECTS

    def __str__(self):
        return f'Story {self.story_number}'    
    
    def get_suspects(self):
        return self.suspect_set.all()
    
    def get_description(self):
        return [suspect.brief for suspect in self.get_suspects()]

