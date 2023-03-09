from django.db import models
from django.core.validators import RegexValidator

class Challenege(models.Model):
    challengeId = models.IntegerField(default=1)
    challengeDesc = models.TextField(default="", max_length=400)


class Fact(models.Model):
    """
    A class representing an environmental fact of the day.

    Attributes:
    -----------
    date : DateField
        The date when the fact will be displayed.
    fact : TextField
        The actual fact that will be displayed on the specified date.

    Methods:
    --------
    __str__()
        Returns a string representation of the object.

    """
    date = models.DateField()
    fact = models.TextField()

    def __str__(self):
        """
        Returns a string representation of the object.
        """
        return f"{self.date} - {self.fact}"


class Bin(models.Model):
    """
    A class representing a recycling bin to be used in challenges and identified on the map.

    Attributes:
    -----------
    bin_number : IntegerField
        The identification number of the bin.
    latitude : FloatField
        The latitude of the bin location.
    longitude : FloatField
        The longitude of the bin location.
    poi_info : TextField
        The point of interest closest to the location of the bin.

    Methods:
    --------
    __str__()
        Returns a string representation of the bin's latitude and longitude.

    """
    bin_number = models.IntegerField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    poi_info = models.TextField(max_length=30)

    def __str__(self):
        """
        Returns a string representation of the object.
        """
        return f'{self.latitude}, {self.longitude}'


class Suspect(models.Model):
    """
    A class representing a suspect in a story/mystery.

    Attributes:
    -----------
    story : ForeignKey
        The story to which the suspect belongs.
    number : IntegerField
        The unique number assigned to the suspect within the story.
    name : TextField
        The name of the suspect.
    brief : TextField
        A brief background/introduction of the suspect.

    Meta:
    ------
    ordering : list
        Specifies the default ordering of the objects returned from the database.

    Methods:
    --------
    save(*args, **kwargs)
        Saves the object to the database. If this is a new object, sets the number attribute to the next available number.

    """
    story = models.ForeignKey(
        'Story', on_delete=models.CASCADE, related_name='suspects', default=0)
    number = models.IntegerField(default=1)
    name = models.TextField(max_length=30, default="")
    brief = models.TextField(max_length=500, default="")

    class Meta:
        ordering = ['number']

    def save(self, *args, **kwargs):
        """
        Saves the object to the database. If this is a new object, sets the number attribute to the next available number.
        """
        if not self.pk:  # if this is a new object being saved
            # get the maximum number currently in the database and increment it by 1
            self.number = self.story.suspects.count() + 1
        super().save(*args, **kwargs)


class Story(models.Model):
    """
    This class represents a Story/mystery

    Attributes:
    -----------
    story_number : IntgerField
        An integer that represents the story number.
    sprite_1 to sprite_5 : CharField
        Single-digit integer value used to assign each sprite in the Unity app of a character to a specific suspect.
    sprite_codes : str
        A string that represents the concatenation of the sprite characters, which is interpreted by the Unity App
    clue1 to clue10 : TextField
        Ten strings that represent clues in the story.
    clues : list
        A list that contains all ten clue strings.
    culprit : CharField
        A integer value that relates the sprite of the culprit to the culprit in the story.
    

    Methods:
    --------
    can_add_suspect()
        Returns True if a new suspect can be added to the story, and False otherwise. 
        Used to make sure that no more than the max (MAX_SUSPECTS) suspects can be added.
    __str__()
        Returns a string representation of the Story object.
    get_suspects()
        Returns a queryset of all Suspect objects related to the story.
    get_description()
        Returns a list of strings containing the brief descriptions of all Suspect objects related to the story. Used in the Unity App to display descriptions.
    getCulprit()
        Returns the sprite integer code of the culprit.
    getSpritesCodes()
        Returns the concatenated string of all sprite codes. Formatted for use in Unity to assign sprite values to suspects.
    getAllClues()
        Returns a list of all ten clue strings.

    """
    MAX_SUSPECTS = 5

    story_number = models.IntegerField(default=1)

    sprite_1 = models.CharField(max_length=1, validators=[
                                RegexValidator(r'^[0-9]+$')])
    sprite_2 = models.CharField(max_length=1, validators=[
                                RegexValidator(r'^[0-9]+$')])
    sprite_3 = models.CharField(max_length=1, validators=[
                                RegexValidator(r'^[0-9]+$')])
    sprite_4 = models.CharField(max_length=1, validators=[
                                RegexValidator(r'^[0-9]+$')])
    sprite_5 = models.CharField(max_length=1, validators=[
                                RegexValidator(r'^[0-9]+$')])

    sprite_codes = str(sprite_1) + str(sprite_2) + \
        str(sprite_3) + str(sprite_4) + str(sprite_5)

    clue1 = models.TextField(max_length=1000, default="")
    clue2 = models.TextField(max_length=1000, default="")
    clue3 = models.TextField(max_length=1000, default="")
    clue4 = models.TextField(max_length=1000, default="")
    clue5 = models.TextField(max_length=1000, default="")
    clue6 = models.TextField(max_length=1000, default="")
    clue7 = models.TextField(max_length=1000, default="")
    clue8 = models.TextField(max_length=1000, default="")
    clue9 = models.TextField(max_length=1000, default="")
    clue10 = models.TextField(max_length=1000, default="")

    clues = [clue1, clue2, clue3, clue4, clue5,
             clue6, clue7, clue8, clue9, clue10]

    culprit = models.CharField(max_length=1, validators=[
                               RegexValidator(r'^[0-9]$')])

    def can_add_suspect(self):
        """
        Returns True if a new suspect can be added to the story, and False otherwise. 
        Used to make sure that no more than the max (MAX_SUSPECTS) suspects can be added.
        """
        return self.suspects.count() < self.MAX_SUSPECTS

    def __str__(self):
        """
        Returns a string representation of the Story object.
        """
        return f'Story {self.story_number}'

    def get_suspects(self):
        """
        Returns a queryset of all Suspect objects related to the story.
        """
        return self.suspect_set.all()

    def get_description(self):
        """
        Returns a list of strings containing the brief descriptions of all Suspect objects related to the story. Used in the Unity App to display descriptions.
        """
        return [suspect.brief for suspect in self.get_suspects()]

    def getCulprit(self):
        """
        Returns the sprite code of the culprit.
        """
        return self.culprit

    def getSpritesCodes(self):
        """
        Returns the concatenated string of all sprite codes. Formatted for use in Unity to assign sprite values to suspects.
        """
        return self.sprite_codes

    def getAllClues(self):
        """
        Returns a list of all ten clue strings.
        """
        return self.clues


