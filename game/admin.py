from django.contrib import admin

# Register your models here.
from game.models import Fact, Bin, Story, Suspect


admin.site.register(Fact)


class BinAdmin(admin.ModelAdmin):
    """Model detailing the configuration of the Django Admin page

    Args:
        admin.ModelAdmin (super): Built-in Django admin structure, adapted by the attributes of this class
    """
    
    # Sets the arrangement of the attributes on the Django Admin page
    list_display = ('bin_number', 'latitude', 'longitude')

# Register the Bin model using the BinAdmin config class
admin.site.register(Bin, BinAdmin)

class SuspectInline(admin.TabularInline):
    model = Suspect
    extra = 0
    max_num = 5
    ordering = ['number']

@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    inlines = [SuspectInline]

# class SuspectInline(admin.TabularInline):
#     model = Suspect


# class StoryAdmin(admin.ModelAdmin):
#     inlines = [SuspectInline]

# admin.site.register(Story, StoryAdmin)