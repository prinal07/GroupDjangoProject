from django import forms
from django.contrib.auth.models import User

from users.models import Profile, Account


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class AccountUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = Account
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
