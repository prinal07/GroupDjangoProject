from django.contrib import admin

from .models import Bin

# Register your models here.
class BinAdmin(admin.ModelAdmin):
    list_display = ('bin_number', 'latitude', 'longitude')
    
admin.site.register(Bin, BinAdmin)