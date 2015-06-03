"""
This script registers the models with the Moderation app
"""
from moderation import moderation
from .models import Post,Event

moderation.register(Post)
moderation.register(Event)