from django.contrib import admin
from moderation.admin import ModerationAdmin

from .models import WYSIWYGPost,MarkdownPost,Event

class WYSIWYGPostAdmin(ModerationAdmin):
    pass

class MarkdownPostAdmin(ModerationAdmin):
    pass

class EventAdmin(ModerationAdmin):
    pass

admin.site.register(WYSIWYGPost,WYSIWYGPostAdmin)
admin.site.register(MarkdownPost,MarkdownPostAdmin)
admin.site.register(Event,EventAdmin)