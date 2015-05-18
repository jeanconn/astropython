from django.contrib import admin

from .models import MarkdownTutorial,CodeTutorial,WYSIWYGTutorial,TutorialSeries

admin.site.register(MarkdownTutorial)
admin.site.register(CodeTutorial)
admin.site.register(WYSIWYGTutorial)
admin.site.register(TutorialSeries)