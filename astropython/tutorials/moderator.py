"""
This script registers the models with the Moderation app
"""
from moderation import moderation
from moderation.moderator import GenericModerator
from .models import Tutorial,TutorialSeries,EducationalResource,CodeSnippet

class Moderator(GenericModerator):
    fields_exclude=['updated','hits']

    def is_auto_approve(self, obj, user):
        if obj.state != "submitted":
            return self.reason('Not Submitted Yet !')
        super(Moderator, self).is_auto_approve(obj, user)

moderation.register(Tutorial,Moderator)
moderation.register(CodeSnippet,Moderator)
moderation.register(TutorialSeries,Moderator)
moderation.register(EducationalResource,Moderator)