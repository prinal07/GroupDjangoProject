from django.contrib import admin
from game.models import Fact, Bin, Story, Suspect, Riddle,GreenArea

admin.site.register(Fact)
admin.site.register(Riddle)

class BinAdmin(admin.ModelAdmin):
    """Model detailing the configuration of the Django Admin page

    Args:
        admin.ModelAdmin (super): Built-in Django admin structure, adapted by the attributes of this class
    """
    
    # Sets the arrangement of the attributes on the Django Admin page
    list_display = ('bin_number', 'latitude', 'longitude')
    exclude = ('challenge',)


# Register the Bin model using the BinAdmin config class
admin.site.register(Bin, BinAdmin)

class SuspectInline(admin.TabularInline):
    """
    Creates an inline form for the Suspect model to be displayed within the Story model's admin interface.

    Attributes:
        model (Suspect): The Suspect model to display in the inline form.
        extra (int): The number of extra forms to display in the inline form.
        max_num (int): The maximum number of forms to display in the inline form.
        ordering (list): A list of field names to use for ordering the forms in the inline form.
    """
    model = Suspect
    extra = 0
    max_num = 5
    ordering = ['number']

@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    """
    Customizes the Story model's admin interface to display inline forms for the Suspect model.

    Attributes:
        inlines (list): A list of inline forms to display in the admin interface.
    """
    inlines = [SuspectInline]

admin.site.register(GreenArea)