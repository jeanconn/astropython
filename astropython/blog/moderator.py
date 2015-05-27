from moderation import moderation
from .models import MarkdownPost,WYSIWYGPost,Events

moderation.register(MarkdownPost)
moderation.register(WYSIWYGPost)
moderation.register(Events)