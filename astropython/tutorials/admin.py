from django.contrib import admin
from django.db import models
from django import forms

from moderation.admin import ModerationAdmin
from django_ace import AceWidget

from .models import MarkdownTutorial,CodeTutorial,WYSIWYGTutorial,TutorialSeries

class CodeModelForm(forms.ModelForm):
    body = forms.CharField(widget=AceWidget(mode='css', theme='twilight'))
    class Meta:
        model=CodeTutorial
        fields="__all__"

class CodeAdmin(ModerationAdmin):
    form=CodeModelForm

class MarkdownTutorialAdmin(ModerationAdmin):
    pass

class WYSIWYGTutorialAdmin(ModerationAdmin):
    pass

class TutorialSeriesAdmin(ModerationAdmin):
    pass

admin.site.register(CodeTutorial,CodeAdmin)
admin.site.register(MarkdownTutorial,MarkdownTutorialAdmin)
admin.site.register(WYSIWYGTutorial,WYSIWYGTutorialAdmin)
admin.site.register(TutorialSeries,TutorialSeriesAdmin)