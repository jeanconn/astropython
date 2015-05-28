from django.contrib import admin
from moderation.admin import ModerationAdmin

from .models import WYSIWYGInput,MarkdownInput

class WYSIWYGInputAdmin(ModerationAdmin):
    pass

class MarkdownInputAdmin(ModerationAdmin):
    pass

admin.site.register(WYSIWYGInput,WYSIWYGInputAdmin)
admin.site.register(MarkdownInput,MarkdownInputAdmin)
