"""
Register models to the admin site from here

All models must inherit fom ModerationAdmin only to enable moderation.
"""
from django.contrib import admin
from django.db import models

from moderation.admin import ModerationAdmin

from .models import MarkdownTutorial,CodeTutorial,WYSIWYGTutorial,TutorialSeries,EducationalResource
from .forms import CodeModelForm

class CodeAdmin(ModerationAdmin):
    form=CodeModelForm # This adds the ACE Code Editor to our Admin website

class MarkdownTutorialAdmin(ModerationAdmin):
    pass

class WYSIWYGTutorialAdmin(ModerationAdmin):
    readonly_fields = ['updated', 'published','created']
    prepopulated_fields = {"slug": ("title",)}

class TutorialSeriesAdmin(ModerationAdmin):
    pass

class EducationalResourceAdmin(ModerationAdmin):
    pass

#Registering the models
admin.site.register(CodeTutorial,CodeAdmin)
admin.site.register(MarkdownTutorial,MarkdownTutorialAdmin)
admin.site.register(WYSIWYGTutorial,WYSIWYGTutorialAdmin)
admin.site.register(TutorialSeries,TutorialSeriesAdmin)
admin.site.register(EducationalResource,EducationalResourceAdmin)