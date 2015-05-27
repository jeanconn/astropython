from django.contrib import admin

from .models import WYSIWYGPost,MarkdownPost,Events

admin.site.register(WYSIWYGPost)
admin.site.register(MarkdownPost)
admin.site.register(Events)