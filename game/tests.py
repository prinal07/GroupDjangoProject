from django.test import TestCase
from .models import *

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
    pass