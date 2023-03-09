from django.contrib import admin
from .models import Account, Profile


class UserAdmin(admin.ModelAdmin):
    """
    Customizes the display of users in the admin panel. Displays the username and whether the user is a university staff member. 

    """
    list_display = ('username', 'is_my_bool_field_true')


admin.site.register(Account, UserAdmin)

admin.site.register(Profile)

class ChallengesInLine(admin.TabularInline):
    """
    Creates an inline form for the Suspect model to be displayed within the Account model's admin interface
    """
    model = Account