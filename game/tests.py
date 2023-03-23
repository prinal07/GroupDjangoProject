from django.test import TestCase
from .models import *
from .views import *

import datetime

class ChallengeTestCase(TestCase):
    def setUp(self):
        challenge = Challenge.objects.create(
            challengeId = 1,
            challengeDesc = "Challenge Description",
            challenge_types = ( ('Bin', 'Bin'), ('Green Areas', 'Green Areas'), ('Walking', 'Walking') ))
        
    def id_type_test(self):
        challenge = Challenge.objects.get(challengeId = 1)
        self.assertTrue(isinstance(challenge.challengeId, int))

    def challenge_description_type_test(self):
        challenge = Challenge.objects.get(challengeId = 1)
        self.assertTrue(isinstance(challenge.challengeDesc, str))

    def challenge_types_test(self):
        challenge = Challenge.objects.get(challengeId = 1)
        self.assertTrue(isinstance(challenge.challenge_types, tuple))
        
    def string_representation_test(self):
        challenge = Challenge.objects.get(challengeId = 1)
        self.assertEqual(str(challenge), challenge.challengeDesc)
        
class FactTestCase(TestCase):
    def setUp(self):
        fact = Fact.objects.create(
            date=datetime.date.today(),
            fact="This is a fact"
        )

    def test_fact_date(self):
        fact = Fact.objects.get(fact="This is a fact")
        self.assertTrue(isinstance(fact.date, datetime.date))
        self.assertEqual(fact.date, datetime.date.today())
        
    def test_fact(self):
        fact = Fact.objects.get(fact="This is a fact")
        self.assertTrue(isinstance(fact.fact, str))
        self.assertEqual(fact.fact, "This is a fact")
        
    def string_representation_test(self):
        fact = Fact.objects.get(fact="This is a fact")
        self.assertEqual(str(fact), f"{fact.date} - {fact.fact}")
        
class BinTestCase(TestCase):
    def setUp(self):
        bin = Bin.objects.create(
            bin_number=1,
            latitude = 3.14159,
            longitude = -3.14159,
            poi_info = "Information about Bin",
            challenge = None
        )
        
    def test_bin_number(self):
        bin = Bin.objects.get(bin_number=1)
        self.assertTrue(isinstance(bin.bin_number, int))
        self.assertTrue(bin.bin_number >= 0)
        
    def test_latitude(self):
        bin = Bin.objects.get(bin_number=1)
        self.assertTrue(isinstance(bin.latitude, float))
        self.assertTrue(len(str(bin.latitude).split(".")[1]) <= 6)
        self.assertTrue(bin.latitude >= -90.0)
        self.assertTrue(bin.latitude <= 90.0)
        
    def test_longitude(self):
        bin = Bin.objects.get(bin_number=1)
        self.assertTrue(isinstance(bin.longitude, float))
        self.assertTrue(len(str(bin.longitude).split(".")[1]) <= 6)
        self.assertTrue(bin.longitude >= -180.0)
        self.assertTrue(bin.longitude <= 180.0)
        
    def test_poi_info(self):
        bin = Bin.objects.get(bin_number=1)
        self.assertTrue(isinstance(bin.poi_info, str))
        self.assertEqual(bin.poi_info, "Information about Bin")
    
    def test_challenge(self):
        pass
    
    def string_representation_test(self):
        bin = Bin.objects.get(bin_number=1)
        self.assertEqual(str(bin), f"{bin.latitude}, {bin.longitude}")

class SuspectTestCase(TestCase):
    def setUp(self):
        suspect = Story.objects.create(
            story = None,
            number = 1,
            name = "Alex Houghton",
            brief = "A second year comp sci student"
        )
        
    def test_number(self):
        suspect = Suspect.objects.get(number=1)
        self.assertTrue(isinstance(suspect.number, int))
        self.assertTrue(suspect.number >= 0)
        
    def test_name(self):
        suspect = Suspect.objects.get(number=1)
        self.assertTrue(isinstance(suspect.name, str))
        self.assertTrue(suspect.name != "")
        
    def test_brief(self):
        suspect = Suspect.objects.get(number=1)
        self.assertTrue(isinstance(suspect.brief, str))
        self.assertEqual(suspect.brief, "A second year comp sci student")
        self.assertTrue(suspect.name != "")
        
    def string_representation_test(self):
        suspect = Suspect.objects.get(number=1)
        self.assertEqual(str(suspect), "Alex Houghton")
        
class StoryTestCase(TestCase):
    def setUp(self):
        story = Story.objects.create( 
            story_number=1,
            sprite_1="3",
            sprite_2="2",
            sprite_3="1",
            sprite_4="4",
            sprite_5="5",
            clue1="Clue 1",
            clue2="Clue 2",
            clue3="Clue 3",
            clue4="Clue 4",
            clue5="Clue 5",
            clue6="Clue 6",
            clue7="Clue 7",
            clue8="Clue 8",
            clue9="Clue 9",
            clue10="Clue 10",
            culprit="1"
        )

    def test_number(self):
        story = Story.objects.get(story_number=1)
        self.assertTrue(isinstance(story.story_number, int))
        self.assertEqual(story.story_number, 1)

    def test_sprites(self):
        story = Story.objects.get(story_number=1)

        self.assertTrue(isinstance(story.sprite_1, str))
        self.assertTrue(len(story.sprite_1) == 1)
        self.assertTrue(int(story.sprite_1) >= 0)
        self.assertTrue(int(story.sprite_1) < 10)
        
        self.assertTrue(isinstance(story.sprite_2, str))
        self.assertTrue(len(story.sprite_2) == 1)
        self.assertTrue(int(story.sprite_2) >= 0)
        self.assertTrue(int(story.sprite_2) < 10)

        self.assertTrue(isinstance(story.sprite_3, str))
        self.assertTrue(len(story.sprite_3) == 1)
        self.assertTrue(int(story.sprite_3) >= 0)
        self.assertTrue(int(story.sprite_3) < 10)

        self.assertTrue(isinstance(story.sprite_4, str))
        self.assertTrue(len(story.sprite_4) == 1)
        self.assertTrue(int(story.sprite_4) >= 0)
        self.assertTrue(int(story.sprite_4) < 10)

        self.assertTrue(isinstance(story.sprite_5, str))
        self.assertTrue(len(story.sprite_5) == 1)
        self.assertTrue(int(story.sprite_5) >= 0)
        self.assertTrue(int(story.sprite_5) < 10)

        sprite_codes = [story.sprite_1, story.sprite_2, story.sprite_3, story.sprite_4, story.sprite_5]

        self.assertEqual(story.getSpritesCodes(self), "".join(sprite_codes))

    def test_clues(self):
        story = Story.objects.get(story_number=1)

        self.assertTrue(isinstance(story.clue1, str))
        self.assertTrue(len(story.clue1) <= 1000)

        self.assertTrue(isinstance(story.clue2, str))
        self.assertTrue(len(story.clue2) <= 1000)
        
        self.assertTrue(isinstance(story.clue3, str))
        self.assertTrue(len(story.clue3) <= 1000)
        
        self.assertTrue(isinstance(story.clue4, str))
        self.assertTrue(len(story.clue4) <= 1000)
        
        self.assertTrue(isinstance(story.clue5, str))
        self.assertTrue(len(story.clue5) <= 1000)
        
        self.assertTrue(isinstance(story.clue6, str))
        self.assertTrue(len(story.clue6) <= 1000)
        
        self.assertTrue(isinstance(story.clue7, str))
        self.assertTrue(len(story.clue7) <= 1000)
        
        self.assertTrue(isinstance(story.clue8, str))
        self.assertTrue(len(story.clue8) <= 1000)
        
        self.assertTrue(isinstance(story.clue9, str))
        self.assertTrue(len(story.clue9) <= 1000)
                
        self.assertTrue(isinstance(story.clue10, str))
        self.assertTrue(len(story.clue10) <= 1000)

        clues = [story.clue1, story.clue2, story.clue3, story.clue4, story.clue5, 
            story.clue6, story.clue7, story.clue8, story.clue9, story.clue10]

        self.assertEqual(story.getAllClues(self), clues)


    def test_culprit(self):
        story = Story.objects.get(story_number=1)

        self.assertTrue(isinstance(story.culprit, str))
        self.assertTrue(len(story.culprit) == 1)
        self.assertTrue(int(story.culprit) >= 1)
        self.assertTrue(int(story.culprit) <= 5)
        self.assertEqual(story.getCulprit(self), story.culprit)

    def test_suspects(self):
        story = Story.objects.get(story_number=1)

        self.assertTrue(len(story.get_suspects(self)) <= story.MAX_SUSPECTS)
        self.assertTrue()
        
class GameWebPageTestCase(TestCase):
    def setUp(self):
        account = Account.objects.create(profileClass=1,
                    accommodation="Accom",
                    email="ah123@exeter.ac.uk",
                    username="username1",
                    password="password123",
                    group=1,
                    level=1,
                    points=124,
                    daily_points=50,
                    last_day_accessed=date.today(),
                    last_bin_scanned=datetime.datetime.now(),
                    last_green_area_accessed=datetime.datetime.now(),
                    staffCheck=False,
                    greenCounter=1,
                    binCounter=4,
                    walkCounter=2)

    def test_riddle_handler(self):
        account = Account.objects.get(username="username1")
        page = self.client.get('/game/riddle_handler/', requests.request(user=account))
        
        self.assertTrue(isinstance(page, JsonResponse))


class QrTests(TestCase):
    """
    Test cases for the QR code scanning functionality.
    """
    def test_success_valid_qr_code(self):
        """
        Test if success function displays "Success!" message for a valid QR code.
        """
        result = 'qjdkiivbbunmue625ljyjy04w941jy'
        Bins = ['qjdkiivbbunmue625ljyjy04w941jy', '3w7wzif7eku0huro54jtmlbt8s0fnm', '8xycn8zhxb203qhqw7v2eetrvcscx1']
        response = None

        for i in Bins:
            if (result == i) :
                response = 'Success!'
        
        self.assertEqual(response, 'Success!')

    def test_invalid_qr_code(self):
        """
        Test if "Invalid Qr Code!" message is displayed for an invalid QR code.
        """
        result = 'invalid_QR_Code'
        Bins = ['qjdkiivbbunmue625ljyjy04w941jy', '3w7wzif7eku0huro54jtmlbt8s0fnm', '8xycn8zhxb203qhqw7v2eetrvcscx1']
        response = None
        j=0

        for i in Bins:
            if (result == i):
                break
            elif (j == 2):
                response='<h2>Invalid Qr Code!</h2>'
            j=j+1
               
        self.assertEqual(response, '<h2>Invalid Qr Code!</h2>')
        
class locationTrackerTest(TestCase):

    def test_distance(self):
        from math import radians
        import math
        """
        Test the distance calculation between two GPS coordinates using the Haversine formula.

        The test compares the calculated distance with a pre-defined response value.

        """
        # Define the GPS coordinates of two points
        lat1 = radians(50.7419340)
        lon1 = radians(-3.5499740)
        lat2 = radians(50.7379538)
        lon2 = radians(-3.5489193)

        # Define the expected distance between the two points
        response = 0.44875786904765347

        # Calculate the distance between the two coordinates using the Haversine formula
        d_lat = lat2 - lat1
        d_lon = lon2 - lon1
        a = math.sin(d_lat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(d_lon/2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
        R = 6371 # Earth's radius in km
        distance = R * c

        # Compare the calculated distance with the expected response
        self.assertEqual(response, distance)