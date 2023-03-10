from django.test import TestCase


import datetime
from .models import *

class AccountTestCase(TestCase):
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

    def test_profile_class_type(self):
        return isinstance(self.account.profileClass, int)

    def test_accomodation_type(self):
        return isinstance(self.account.accomodation, str)

    def test_email_type(self):
        return isinstance(self.account.email, str)

    def test_username_type(self):
        return isinstance(self.account.username, str)

    def test_password_type(self):
        return isinstance(self.account.password, str)

    def test_group_type(self):
        return isinstance(self.account.group, int)

    def test_level_type(self):
        return isinstance(self.account.level, int)

    def test_points_type(self):
        return isinstance(self.account.points, int)

    def test_daily_points_type(self):
        return isinstance(self.account.daily_points, int)

    def test_last_day_type(self):
        return isinstance(self.account.last_day_accessed, datetime.Datetime)

    def test_staff_type(self):
        return isinstance(self.account.staffCheck, bool)

    def test_profileClass_range(self):
        if self.account.profileClass < 0:
            return False
        elif self.account.profileClass > 2:
            return False
        else:
            return True
    
    def test_exeter_email(self):
        return self.account.email.split("@")[1] == "exeter.ac.uk"

    def test_level_minimum(self):
        return self.account.level < 1
    
    def test_points_minimum(self):
        return self.account.points < 0

    def test_daily_points_minimum(self):
        return self.account.daily_points < 0

    def test_last_day_future(self):
        return self.account.last_day_accessed > datetime.now()

    def test_staffCheck_null(self):
        return staffCheck != None
    
class ProfileTestCase(TestCase):
    def setUp(self):
        profile = Profile(user=1,
                          image=open("../media/default.jpg")

    def test_user_key_type():
        return isinstance(self.profile.user, int)

    def test_image_type():
        return isinstnace(self.profile.image, file)

    def test_user_in_database():
        if self.profile.user > 0:
            if self.profile.user < len(Profile.objects.all()) + 1:
                return True

        return False
