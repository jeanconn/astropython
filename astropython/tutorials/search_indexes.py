import datetime
from haystack import indexes
from .models import *


class TutorialIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title')
    abstract =indexes.CharField(model_attr='abstract')
    body= indexes.CharField(model_attr='body')

    def get_model(self):
        return Tutorial