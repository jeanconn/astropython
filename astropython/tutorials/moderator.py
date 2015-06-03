"""
This script registers the models with the Moderation app
"""
from moderation import moderation
from .models import Tutorial,TutorialSeries,EducationalResource,CodeSnippet,SeriesTutorial

moderation.register(Tutorial)
moderation.register(CodeSnippet)
moderation.register(TutorialSeries)
moderation.register(SeriesTutorial)
moderation.register(EducationalResource)