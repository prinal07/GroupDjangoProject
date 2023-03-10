from django.contrib import admin
from .models import Account
from game.models import Challenge
from django.db import models
from users.models import Account
from game.models import Challenge

from django.contrib import admin
from .models import Account, Challenge


class ChallengeStatus(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.account.username} - {self.challenge.challengeDesc}"
    
    def isCompleted(self):
        return self.completed

    
class ChallengeStatusInLine(admin.TabularInline):
    model = ChallengeStatus
    extra = 1

class AccountAdmin(admin.ModelAdmin):
    inlines = [ChallengeStatusInLine]
    exclude = ('challenges',)

    
admin.site.register(Account, AccountAdmin)

admin.site.register(Challenge)

