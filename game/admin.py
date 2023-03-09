from django.contrib import admin

# Register your models here.
from game.models import Fact, Bin, Story, Suspect


admin.site.register(Fact)


class BinAdmin(admin.ModelAdmin):
    list_display = ('bin_number', 'latitude', 'longitude')


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