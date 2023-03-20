from django.http import HttpResponse
from django.test import TestCase


import datetime
import os
import PIL
from .models import *
from .views import *
from django.contrib.auth.models import User

class AccountTestCase(TestCase):
    """Test harness for the Account model defined in ./models.py:Account 
    Creates a mock object and tests the type  
    
    Args:
        TestCase (super): Django's Built-in Testing harness, for which the methods in this class 
        are applied in conjunction with

    Methods:
        setUp(): Create mock object, for use in the AccountTestCase 
        test_profile_class_type(): Tests type of the profileClass attribute
        test_accommodation_type(): Tests type of the accommodation attribute
        test_email_type(): Tests type of the email attribute
        test_username_type(): Tests type of the username attribute
        test_password_type(): Tests type of the password attribute
        test_group_type(): Tests type of the group attribute
        test_level_type(): Tests type of the level attribute
        test_points_type(): Tests type of the points attribute
        test_daily_points_type(): Tests type of the daily_points attribute
        test_last_day_type(): Tests type of last_day_accessed attribute
        test_staff_type(): Tests type of the staffCheck attribute
        test_profileClass_range(): Tests range of the profileClass attribute from [0..2]
        test_exeter_email(): Tests email is of the domain "exeter.ac.uk"
        test_level_minimum(): Tests if Account level is above the minimum (1)
        test_points_minimum(): Tests if Account points is above the minimum (0)
        test_daily_points_minimum(): Tests if Daily Points is above the minimum (0)
        test_last_day_future(): Tests if the Last Accessed day is in the future
        test_staffCheck_null(): Tests if staffCheck is populated

    """

    def setUp(self):
        challenge = Challenge.objects.create(challengeId = 1)
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
        account.challenges.add(challenge)

        self.VALID_EMAIL_DOMAIN = "exeter.ac.uk"
        self.MINIMUM_LEVEL = 1
        self.MINIMUM_POINTS = 0
        self.MINIMUM_PROFILE_CLASS = 0
        self.MAXIMUM_PROFILE_CLASS = 2

    def test_profile_class_type(self):
        account = Account.objects.get(username="username1")
        self.assertTrue(isinstance(account.profileClass, int))
        
    def test_accommodation_type(self):
        account = Account.objects.get(username="username1")
        self.assertTrue(isinstance(account.accommodation, str))

    def test_email_type(self):
        account = Account.objects.get(username="username1")
        self.assertTrue(isinstance(account.email, str))

    def test_username_type(self):
        account = Account.objects.get(username="username1")
        self.assertTrue(isinstance(account.username, str))

    def test_password_type(self):
        account = Account.objects.get(username="username1")
        self.assertTrue(isinstance(account.password, str))

    def test_group_type(self):
        account = Account.objects.get(username="username1")
        self.assertTrue(isinstance(account.group, int))

    def test_level_type(self):
        account = Account.objects.get(username="username1")
        self.assertTrue(isinstance(account.level, int))

    def test_points_type(self):
        account = Account.objects.get(username="username1")
        self.assertTrue(isinstance(account.points, int))

    def test_daily_points_type(self):
        account = Account.objects.get(username="username1")
        self.assertTrue(isinstance(account.daily_points, int))

    def test_last_day_type(self):
        account = Account.objects.get(username="username1")
        self.assertTrue(isinstance(account.last_day_accessed, datetime.date))

    def test_last_bin_scan_time(self):
        account = Account.objects.get(username="username1")
        self.assertTrue(isinstance(account.last_bin_scanned, datetime.datetime))
        self.assertTrue(account.last_bin_scanned <= datetime.datetime.now())
        
    def test_last_green_area_time(self):
        account = Account.objects.get(username="username1")
        self.assertTrue(isinstance(account.last_green_area_accessed, datetime.datetime))
        self.assertTrue(account.last_bin_scanned <= datetime.datetime.now())

    def test_staff_type(self):
        account = Account.objects.get(username="username1")
        self.assertTrue(isinstance(account.staffCheck, bool))

    def test_profileClass_range(self):
        account = Account.objects.get(username="username1")
        self.assertTrue(isinstance(account.profileClass, int))
        self.assertTrue(account.profileClass >= self.MINIMUM_PROFILE_CLASS)
        self.assertTrue(account.profileClass <= self.MAXIMUM_PROFILE_CLASS)
    
    def test_exeter_email(self):
        account = Account.objects.get(username="username1")
        self.assertTrue(isinstance(account.email, str))
        self.assertEquals(account.email.split("@")[1], self.VALID_EMAIL_DOMAIN)

    def test_level_minimum(self):
        account = Account.objects.get(username="username1")
        self.assertTrue(account.level >= self.MINIMUM_LEVEL)
    
    def test_points_minimum(self):
        account = Account.objects.get(username="username1")
        self.assertTrue(account.points >= self.MINIMUM_POINTS)

    def test_daily_points_minimum(self):
        account = Account.objects.get(username="username1")
        self.assertTrue(account.daily_points > self.MINIMUM_POINTS)

    def test_last_day_future(self):
        account = Account.objects.get(username="username1")
        self.assertTrue(account.last_day_accessed <= datetime.date.today())

    def test_staffCheck_null(self):
        account = Account.objects.get(username="username1")
        self.assertTrue(isinstance(account.staffCheck, bool))
        self.assertIsNot(account.staffCheck, None)
    
    def test_challenges(self):
        pass
    
    def test_green_counter(self):
        account = Account.objects.get(username="username1")
        self.assertTrue(isinstance(account.greenCounter, int))
        self.assertTrue(account.greenCounter >= 0)
    
    def test_bin_counter(self):
        account = Account.objects.get(username="username1")
        self.assertTrue(isinstance(account.binCounter, int))
        self.assertTrue(account.binCounter >= 0)
    
    def test_walk_counter(self):
        account = Account.objects.get(username="username1")
        self.assertTrue(isinstance(account.walkCounter, int))
        self.assertTrue(account.walkCounter >= 0)
        
    def test_start_latitude(self):
        account = Account.objects.get(username="username1")
        self.assertTrue(isinstance(account.startingLat, float))
        self.assertTrue(account.startingLat >= -90.0)
        self.assertTrue(account.startingLat <= 90.0)
        
    def test_start_longitude(self):
        account = Account.objects.get(username="username1")
        self.assertTrue(isinstance(account.startingLng, float))
        self.assertTrue(account.startingLng >= -180.0)
        self.assertTrue(account.startingLng <= 180.0)
        
    def test_distance_travelled(self):
        account = Account.objects.get(username="username1")
        self.assertTrue(float(account.distanceTraveled) > 0.0)
        self.assertTrue(False not in [i in ["0","1","2","3","4","5","6","7","8","9","."] for i in account.distanceTraveled])
    
    def test_game_complete(self):
        account = Account.objects.get(username="username1")
        self.assertTrue(isinstance(account.gameCompleted, int))
        self.assertTrue(account.gameCompleted >= 0)
        
    def test_clues(self):
        account = Account.objects.get(username="username1")
        self.assertTrue(isinstance(account.cluesUnlocked, int))
        self.assertTrue(account.cluesUnlocked >= 0)
        
    def test_riddle_done(self):
        account = Account.objects.get(username="username1")
        self.assertTrue(isinstance(account.riddleDone, bool))
        self.assertTrue(account.riddleDone != None)
    
    def test_riddle_status(self):
        account = Account.objects.get(username="username1")
        self.assertTrue(isinstance(account.riddle_message_status, str))
        self.assertTrue(len(account.riddle_message_status) <= 100)
    
    def string_representation_test(self):
        account = Account.objects.get(username="usernamae1")
        self.assertEqual(str(account), account.username)
    
class ProfileTestCase(TestCase):
    """Profile Model Test Harness

    Args:
        TestCase (super): Django's Built-In Test Harness structure, to work with methods in this class

    Methods:
        setUp(): Create a mock object
        test_user_key_type(): Tests if Profile type in model is valid
        test_image_type(): Tests if Profile image is a valid type
        test_user_in_database(): Tests if Profile User is in the Users database
    """
    def setUp(self):
        img_path = os.getcwd()
        img_path += "\\media\\default.jpg"

        mock_user = User.objects.create(username="username1")
        self.profile = Profile.objects.create()
        self.profile.user = mock_user

    def test_user_key_type(self):
        self.assertTrue(isinstance(self.profile.user, User))

    def test_user_in_database(self):
        self.assertTrue(self.profile.user in User.objects.all())

    def string_representation_test(self):
        self.assertEqual(str(self.profile.user), f"{self.profile.user.username} Profile")
        
class ChallengeTrackerTestCase(TestCase):
    def setUp(self):
        pass
    
    def test_tracker_account_type(self):
        pass
    
    def test_tracker_challenge_type(self):
        pass
    
    def test_tracker_completed_type(self):
        pass
    
    def string_representation_test(self):
        pass
    
    def completedTest(self):
        pass
    
class WebResponseTestCase(TestCase):
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
        
    def test_register_page(self):
        page = self.client.get('register/')
        self.assertTrue(isinstance(page, HttpResponse))
        