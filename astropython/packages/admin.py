"""
Register models to the admin site from here

All models must inherit fom ModerationAdmin only to enable moderation.
"""
from django.contrib import admin
from moderation.admin import ModerationAdmin

from .models import WYSIWYGInput,MarkdownInput

class WYSIWYGInputAdmin(ModerationAdmin):
    pass

class MarkdownInputAdmin(ModerationAdmin):
    pass

#Registering the models
admin.site.register(WYSIWYGInput,WYSIWYGInputAdmin)
admin.site.register(MarkdownInput,MarkdownInputAdmin)
