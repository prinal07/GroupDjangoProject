from django.contrib import admin
from .models import Account, Profile


# Register your models here.

# Defines a representation of a model for the Django Admin site
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'is_my_bool_field_true')

# Registers models to be visible on the site
# Registers Account model using the UserAdmin config
admin.site.register(Account, UserAdmin)
admin.site.register(Profile)
