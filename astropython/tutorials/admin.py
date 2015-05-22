from django.contrib import admin
from django.db import models

from django_ace import AceWidget

from .models import MarkdownTutorial,CodeTutorial,WYSIWYGTutorial,TutorialSeries

class CodeAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AceWidget},
    }

admin.site.register(CodeTutorial,CodeAdmin)
admin.site.register(MarkdownTutorial)
admin.site.register(WYSIWYGTutorial)
admin.site.register(TutorialSeries)