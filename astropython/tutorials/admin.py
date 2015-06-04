"""
Register models to the admin site from here

All models must inherit fom ModerationAdmin only to enable moderation.
"""
from django.contrib import admin
from django.db import models

from moderation.admin import ModerationAdmin

from .models import Tutorial,TutorialSeries,EducationalResource,CodeSnippet,SeriesTutorial

class CodeAdmin(ModerationAdmin):
    #form=CodeModelForm # This adds the ACE Code Editor to our Admin website
    pass

class TutorialAdmin(ModerationAdmin):
    readonly_fields = ['updated', 'published','created']
    prepopulated_fields = {"slug": ("title",)}

class EducationalResourceAdmin(ModerationAdmin):
    pass

class TutorialSeriesAdmin(ModerationAdmin):
    pass


#Registering the models
admin.site.register(CodeSnippet,CodeAdmin)
admin.site.register(Tutorial,TutorialAdmin)
admin.site.register(TutorialSeries,TutorialSeriesAdmin)
admin.site.register(SeriesTutorial)
admin.site.register(EducationalResource,EducationalResourceAdmin)