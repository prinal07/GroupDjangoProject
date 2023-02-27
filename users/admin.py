from django.contrib import admin
from .models import User, Profile


# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'is_my_bool_field_true')


admin.site.register(User, UserAdmin)

admin.site.register(Profile)
