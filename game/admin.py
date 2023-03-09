from django.contrib import admin
from game.models import Fact, Bin, Story, Suspect

admin.site.register(Fact)

class BinAdmin(admin.ModelAdmin):
    """
    Customizes the Bin model's admin interface to display specific fields in the list view.

    Attributes:
        list_display (tuple): A tuple of field names to display in the list view.
    """
    list_display = ('bin_number', 'latitude', 'longitude')

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
