from moderation import moderation
from .models import MarkdownPost,WYSIWYGPost,Event

moderation.register(MarkdownPost)
moderation.register(WYSIWYGPost)
moderation.register(Event)