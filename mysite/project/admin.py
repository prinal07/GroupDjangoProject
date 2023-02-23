from django.contrib import admin

from .models import User, Group, Challenge, Accomodation, Department

admin.site.register(User)
admin.site.register(Group)
admin.site.register(Challenge)
admin.site.register(Accomodation)
admin.site.register(Department)
