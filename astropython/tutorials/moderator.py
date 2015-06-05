"""
This script registers the models with the Moderation app
"""
from moderation import moderation
from moderation.moderator import GenericModerator
from .models import Tutorial,TutorialSeries,EducationalResource,CodeSnippet

class TutorialModerator(GenericModerator):
    fields_exclude=['updated','hits']

class SnippetModerator(GenericModerator):
    fields_exclude=['updated','hits']

class ResourceModerator(GenericModerator):
    fields_exclude=['updated','hits']

class SeriesModerator(GenericModerator):
    fields_exclude=['updated','hits']

moderation.register(Tutorial,TutorialModerator)
moderation.register(CodeSnippet,SnippetModerator)
moderation.register(TutorialSeries,SeriesModerator)
moderation.register(EducationalResource,ResourceModerator)