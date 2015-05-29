"""
This script registers the models with the Moderation app
"""

from moderation import moderation
from .models import MarkdownInput,WYSIWYGInput

moderation.register(MarkdownInput)
moderation.register(WYSIWYGInput)
