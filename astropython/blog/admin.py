"""
Register models to the admin site from here

All models must inherit fom ModerationAdmin only to enable moderation.
"""
from django.contrib import admin
from moderation.admin import ModerationAdmin

from .models import Post,Event


class PostAdmin(ModerationAdmin):
    pass

class EventAdmin(ModerationAdmin):
    pass

#Registering the models
admin.site.register(Post,PostAdmin)
admin.site.register(Event,EventAdmin)