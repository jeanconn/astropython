from django.contrib import admin
from django.db import models
from django import forms

from django_ace import AceWidget

from .models import MarkdownTutorial,CodeTutorial,WYSIWYGTutorial,TutorialSeries

class CodeModelForm(forms.ModelForm):
    body = forms.CharField(widget=AceWidget(mode='css', theme='twilight'))
    class Meta:
        model=CodeTutorial
        fields="__all__"

class CodeAdmin(admin.ModelAdmin):
    form=CodeModelForm

admin.site.register(CodeTutorial,CodeAdmin)
admin.site.register(MarkdownTutorial)
admin.site.register(WYSIWYGTutorial)
admin.site.register(TutorialSeries)