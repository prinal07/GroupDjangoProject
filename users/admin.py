from django.contrib import admin
from .models import Account, Profile
from game.models import Bin, Challenge

# class UserAdmin(admin.ModelAdmin):
#     """
#     Customizes the display of users in the admin panel. Displays the username and whether the user is a university staff member. 

#     """
#     list_display = ('username', 'is_my_bool_field_true')

# admin.site.register(Account, UserAdmin)

admin.site.register(Profile)

# class BinInLine(admin.TabularInline):
#     model = Bin
#     extra = 0

# @admin.register(Challenge)
# class ChallengeAdmin(admin.ModelAdmin):
#     inlines = [BinInLine]

# class ChallengeInLine(admin.TabularInline):
#     model = Challenge
#     extra = 0

# @admin.register(Account)
# class ChallengeAdmin(admin.ModelAdmin):
#     inlines = [ChallengeInLine]

# class AccountAdmin(admin.ModelAdmin):
#     """
#     Customizes the display of users in the admin panel. Displays the username and whether the user is a university staff member. 
#     """
#     inlines = [ChallengeInLine]
#     list_display = ('username', 'is_my_bool_field_true')

# admin.site.register(Account, AccountAdmin)

# class ChallengeInLine(admin.TabularInline):
#     model = Challenge
#     extra = 0


# @admin.register(Account)
# class AccountAdmin(admin.ModelAdmin):
#     """
#     Customizes the display of users in the admin panel. Displays the username and whether the user is a university staff member. 
#     """
#     inlines = [ChallengeInLine]
#     list_display = ('username', 'is_my_bool_field_true')

#     def get_queryset(self, request):
#         qs = super().get_queryset(request)
#         return qs.prefetch_related('challenges')
    

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


# class ChallengeInLine(admin.TabularInline):
#     model = Account.challenges.through
#     extra = 1

# class AccountAdmin(admin.ModelAdmin):
#     inlines = [ChallengeInLine]


    
class ChallengeStatusInLine(admin.TabularInline):
    model = ChallengeStatus
    extra = 1

class AccountAdmin(admin.ModelAdmin):
    inlines = [ChallengeStatusInLine]
    
admin.site.register(Account, AccountAdmin)

admin.site.register(Challenge)

