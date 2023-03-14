
from django.db import models
from django.core.validators import RegexValidator

class Challenge(models.Model):
    challengeId = models.IntegerField(default=1)
    challengeDesc = models.TextField(default="", max_length=400)
    CHALLENGE_TYPES = (
        ('Bin', 'Bin'),
        ('Green Areas', 'Green Areas'),
        ('Walking', 'Walking')
    )
    challengeType = models.TextField(choices=CHALLENGE_TYPES, default='')             

    def __str__(self):
        return self.challengeDesc

class Fact(models.Model):
    """Fact model used to store the fact of the day.
    Stores simply a date and a string to be fetched by Django each day

    Args:
        models.Model (super): Built-in Djagno type structure, adapted by the attributes of this class

    Methods:
        __str__(): String representation function of this class
        
    """
    date = models.DateField()
    fact = models.TextField()

    def __str__(self):
        """Method to represent the model to the user within the program

        Returns:
            string: Formatted string using attributes from the model to show information "(date, fact)"
        """
        return f"{self.date} - {self.fact}"

class Bin(models.Model):
    """Bin model to store information to be presented on the map at <url>/game/map/
    Stores Longitude/Latitude floats, a string for information, and an Integer to identify

    Args:
        models.Model (super): Built-in Django type structure, adapted by the attributes of this class

    Methods:
        __str__(): String representation function of this class

    """
    bin_number = models.IntegerField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    poi_info = models.TextField(max_length=30)
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE, null=True)

    def __str__(self):
        """Method to represent the model to the user within the program

        Returns:
            string: Formatted string using attributes from the model to show information "(Lat, Lon)"
        """
        return f'{self.latitude}, {self.longitude}'

class Suspect(models.Model):
    """Suspect model, to store information to be used in the Mystery minigame at <url>/game/unity
    Stores a Foreign Key to a Story object, an ID Number, a name, and a brief

    Args:
        models.Model (super): Built-in Django type structure, adapted by the attributes of this class
        
    Methods:
        class Meta: Defines metadata to be used in the Django Admin site regarding this model
        save(): Increments the pk of the temporary model before committing to the database
    """
    
    # Refers to a Story record in the Database
    story = models.ForeignKey('Story', on_delete=models.CASCADE, related_name='suspects', default=0)
    number = models.IntegerField(default=1)
    name = models.TextField(max_length=30, default="")
    brief = models.TextField(max_length=500, default="")

    class Meta:
        """Django admin metadata class
        """
        # Tells Django admin to order by the number attribute value in descending order
        ordering = ['number']

    def save(self, *args, **kwargs):
        """Saves the Suspect model to the Database as a new record
        Overloads the existing models.Model.save() function
        """
        if not self.pk:  # if this is a new object being saved
            # get the maximum number currently in the database and increment it by 1
            self.number = self.story.suspects.count() + 1
        super().save(*args, **kwargs)

    def getDescription(self):
        return self.brief
    

class Story(models.Model):
    """Story model to be passed into the Mystery game at <url>/game/unity/
    Defines all information to be used in the game

    Args:
        models.Model (super): Built-in Django type structure, adapted by the attributes of this class

    Methods:
        can_add_suspect(): Determine current number of suspects currently picked is less than constant MAX_SUSPECTS
        __str__(): String Representation function of this class
        get_suspects(): Get Current suspects in the Story model
        get_description(): Get the description attribute for every suspect in the Story 
        getCulprit(): Get the index code of the culprit
        getSpriteCodes(): Get the string of sprite_codes "12345" style
        getAllClues(): Get all clues currently created in the Story
    """
    
    # Constant to limit expansion of the model contents
    MAX_SUSPECTS = 5
    
    # Identification number to retrieve models by
    story_number = models.IntegerField(default=1)

    # Collection of sprite codes, valid numbers from 0-9, validated using regex
    # Numbers 0-9 correlate to sprite files in the Unity Game build, named "character_sprite_x.png"
    sprite_1 = models.CharField(max_length=1, validators=[RegexValidator(r'^[0-9]+$')])
    sprite_2 = models.CharField(max_length=1, validators=[RegexValidator(r'^[0-9]+$')])
    sprite_3 = models.CharField(max_length=1, validators=[RegexValidator(r'^[0-9]+$')])
    sprite_4 = models.CharField(max_length=1, validators=[RegexValidator(r'^[0-9]+$')])
    sprite_5 = models.CharField(max_length=1, validators=[RegexValidator(r'^[0-9]+$')])

    # Codes are concatenated into a string, to customise the appearance of the sprites in-game
    # In the unity project, a C# Function title SetSuspectSprites correlates each index to a sprite object
    sprite_codes = (sprite_1) + (sprite_2) + (sprite_3) + (sprite_4) + (sprite_5)

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
    
    # Collects the clues to a list, to be sent to the Unity file as context
    clues = [clue1, clue2, clue3, clue4, clue5, clue6, clue7, clue8, clue9, clue10]
    
    # Assigns the culprit to an index of the five available characters
    culprit = models.CharField(max_length=1, validators=[RegexValidator(r'^[0-4]$')])
    
    def can_add_suspect(self):
        """Check to determine if the maximum number of suspects has been reached

        Returns:
            bool: If condition checking suspect count to the maximum
        """
        return self.suspects.count() < self.MAX_SUSPECTS

    def __str__(self):
        """String Formatting Function to display the Story model to the user

        Returns:
            string: Formatted string, displaying the Story ID Number
        """
        return f'Story {self.story_number}'    
    
    def get_suspects(self):
        """Function to return the models of the attached Suspects to an individual Story object

        Returns:
            [Suspect]: Members of the suspect_set list in the current model
        """
        return self.suspect_set.all()

    def get_description(self):
        """Function to return the descriptions of each Suspect attached to an individual Story object

        Returns:
            [string]: Descriptions of Story suspects
        """
        return [suspect.brief for suspect in self.get_suspects()]

    def getCulprit(self):
        """Function to return the character that signifies the Culprit of the story

        Returns:
            string: Index of the culprit within this story model 
        """
        return self.culprit

    def getSpritesCodes(self):
        """Function to return the sprite codes string to use in the Unity Game, to customise the appearance of suspects

        Returns:
            string: Sprite code representation of the appearance in this Story model
        """
        return self.sprite_codes

    def getAllClues(self):
        """Function to return all supplied clues for this story, to be presented to the user

        Returns:
            [string]: List of clue descriptions, for use in the Unity Game 
        """
        return self.clues
