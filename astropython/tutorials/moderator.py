"""
This script registers the models with the Moderation app
"""
from moderation import moderation
from .models import WYSIWYGTutorial,CodeTutorial,MarkdownTutorial,TutorialSeries,EducationalResource

moderation.register(WYSIWYGTutorial)
moderation.register(CodeTutorial)
moderation.register(MarkdownTutorial)
moderation.register(TutorialSeries)
moderation.register(EducationalResource)