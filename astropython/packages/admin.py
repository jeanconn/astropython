"""
Register models to the admin site from here

All models must inherit fom ModerationAdmin only to enable moderation.
"""
from django.contrib import admin
from moderation.admin import ModerationAdmin

from .models import Package

class PackageAdmin(ModerationAdmin):
    pass

#Registering the models
admin.site.register(Package,PackageAdmin)
