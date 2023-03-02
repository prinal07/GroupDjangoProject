from django.contrib import admin

# Register your models here.
from player.models import Fact, Bin

admin.site.register(Fact)


class BinAdmin(admin.ModelAdmin):
    list_display = ('bin_number', 'latitude', 'longitude')


admin.site.register(Bin, BinAdmin)
