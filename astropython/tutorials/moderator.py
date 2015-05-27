from moderation import moderation
from .models import WYSIWYGTutorial,CodeTutorial,MarkdownTutorial,TutorialSeries

moderation.register(WYSIWYGTutorial)
moderation.register(CodeTutorial)
moderation.register(MarkdownTutorial)
moderation.register(TutorialSeries)