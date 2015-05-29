"""
Register models to the admin site from here

All models must inherit fom ModerationAdmin only to enable moderation.
"""
from django.contrib import admin
from django.db import models

from moderation.admin import ModerationAdmin

from .models import MarkdownTutorial,CodeTutorial,WYSIWYGTutorial,TutorialSeries
from .forms import CodeModelForm

class CodeAdmin(ModerationAdmin):
    form=CodeModelForm # This adds the ACE Code Editor to our Admin website

class MarkdownTutorialAdmin(ModerationAdmin):
    pass

class WYSIWYGTutorialAdmin(ModerationAdmin):
    pass

class TutorialSeriesAdmin(ModerationAdmin):
    pass

#Registering the models
admin.site.register(CodeTutorial,CodeAdmin)
admin.site.register(MarkdownTutorial,MarkdownTutorialAdmin)
admin.site.register(WYSIWYGTutorial,WYSIWYGTutorialAdmin)
admin.site.register(TutorialSeries,TutorialSeriesAdmin)