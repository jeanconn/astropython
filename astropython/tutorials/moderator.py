"""
This script registers the models with the Moderation app
"""
from moderation import moderation
from .models import Tutorial,TutorialSeries,EducationalResource,CodeSnippet

moderation.register(Tutorial)
moderation.register(CodeSnippet)
moderation.register(TutorialSeries)
moderation.register(EducationalResource)