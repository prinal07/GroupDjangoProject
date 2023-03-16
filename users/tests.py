from django.test import TestCase


import datetime
from .models import *
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
        test_accomodation_type(): Tests type of the accomodation attribute
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
        account = Account(profileClass=1,
                          accomodation="Accom",
                          email="ah123@exeter.ac.uk",
                          username="username1",
                          password="password123",
                          group=1,
                          level=1,
                          points=124,
                          daily_points=50,
                          last_day_accessed=None,
                          staffCheck=False)

        self.VALID_EMAIL_DOMAIN = "exeter.ac.uk"
        self.MINIMUM_LEVEL = 1
        self.MINIMUM_POINTS = 0

    #     def test_profile_class_type(self):
    #         return isinstance(self.account.profileClass, int)
    #
    #     def test_accomodation_type(self):
    #         return isinstance(self.account.accomodation, str)
    #
    #     def test_email_type(self):
    #         return isinstance(self.account.email, str)
    #
    #     def test_username_type(self):
    #         return isinstance(self.account.username, str)
    #
    #     def test_password_type(self):
    #         return isinstance(self.account.password, str)
    #
    #     def test_group_type(self):
    #         return isinstance(self.account.group, int)
    #
    #     def test_level_type(self):
    #         return isinstance(self.account.level, int)
    #
    #     def test_points_type(self):
    #         return isinstance(self.account.points, int)
    #
    #     def test_daily_points_type(self):
    #         return isinstance(self.account.daily_points, int)
    #
    #     def test_last_day_type(self):
    #         return isinstance(self.account.last_day_accessed, datetime.Datetime)
    #
    #     def test_staff_type(self):
    #         return isinstance(self.account.staffCheck, bool)
    #
    #     def test_profileClass_range(self):
    #         if self.account.profileClass < 0:
    #             return False
    #         elif self.account.profileClass > 2:
    #             return False
    #         else:
    #             return True
    #
    #     def test_exeter_email(self):
    #         return self.account.email.split("@")[1] == self.VALID_EMAIL_DOMAIN
    #
    #     def test_level_minimum(self):
    #         return self.account.level >= self.MINIMUM_LEVEL
    #
    #     def test_points_minimum(self):
    #         return self.account.points > self.MINIMUM_POINTS
    #
    #     def test_daily_points_minimum(self):
    #         return self.account.daily_points > self.MINIMUM_POINTS
    #
    #     def test_last_day_future(self):
    #         return self.account.last_day_accessed > datetime.now()
    #
    #     def test_staffCheck_null(self):
    #         return staffCheck != None
    #
    # class ProfileTestCase(TestCase):
    """Profile Model Test Harness

    Args:
        TestCase (super): Django's Built-In Test Harness structure, to work with methods in this class

    Methods:
        setUp(): Create a mock object
        test_user_key_type(): Tests if Profile type in model is valid
        test_image_type(): Tests if Profile image is a valid type
        test_user_in_database(): Tests if Profile User is in the Users database
    """
    # def setUp(self):
    #     if len(User.objects.all()) != 0:
    #         profile = Profile(user=User.objects.all()[0],
    #                           image=open("../media/default.jpg")
    #     else:
    #         user = User()
    #         profile = Profile(user=user,
    #                           image=open("../media/default.jpg")
    # def test_user_key_type():
    #     return isinstance(self.profile.user, User)
    #
    # def test_image_type():
    #     return isinstnace(self.profile.image, file)
    #
    # def test_user_in_database():
    #     if self.profile.user == User():
    #         return True
    #
    #     return self.profile.user in User.objects.all():
