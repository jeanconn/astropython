"""
Register models to the admin site from here

All models must inherit fom ModerationAdmin only to enable moderation.
"""
from django.contrib import admin
from django.db import models

from moderation.admin import ModerationAdmin

from .models import *

class Admin(ModerationAdmin):
    readonly_fields = ['updated','created']
    prepopulated_fields = {"slug": ("title",)}

#Registering the models

admin.site.register(Tutorial,Admin)
admin.site.register(Snippet,Admin)
admin.site.register(Wiki,Admin)
admin.site.register(Announcement,Admin)
admin.site.register(News,Admin)
admin.site.register(Blog,Admin)
admin.site.register(Package,Admin)
admin.site.register(TutorialSeries,Admin)
admin.site.register(SeriesTutorial)
admin.site.register(EducationalResource,Admin)
admin.site.register(Event,Admin)