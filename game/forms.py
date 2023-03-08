from django import forms
from django.contrib.auth.models import User

from users.models import Profile, Account

#Update Django's user
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

#Update User Account
class AccountUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = Account
        fields = ['username', 'email']


# Update profile pic
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']


# delete account
class DeleteAccountForm(forms.Form):
    confirm_delete = forms.BooleanField(
        required=True,
        label='Confirm deletion',
        help_text="Tick the box to confirm account deletion."
    )
