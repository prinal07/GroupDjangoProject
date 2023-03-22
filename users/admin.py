from django.contrib import admin
from .models import Account
from game.models import Challenge
from django.db import models
from users.models import Account
from game.models import Challenge
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from users.models import Account
from django.contrib.auth.models import User
from django.contrib import admin
from .models import Account, Challenge, Profile, ChallengeTracker

class ChallengeStatusInLine(admin.TabularInline):
    model = ChallengeTracker
    extra = 1

class AccountAdmin(admin.ModelAdmin):
    list_display = ('username', 'is_my_bool_field_true')
    inlines = [ChallengeStatusInLine]
    exclude = ('challenges',)

    
admin.site.register(Account, AccountAdmin)
admin.site.register(Challenge)
admin.site.register(Profile)

