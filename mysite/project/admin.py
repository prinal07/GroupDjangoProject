from django.contrib import admin

from .models import User, Group, Challenge

admin.site.register(User)
admin.site.register(Group)
admin.site.register(Challenge)

