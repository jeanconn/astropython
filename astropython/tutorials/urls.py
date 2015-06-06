from django.conf.urls import patterns,url,include

from .models import Tutorial,CodeSnippet,EducationalResource,TutorialSeries,SeriesTutorial
from .views import create,single,vote,all,single_series,edit

urlpatterns = patterns('',
    url(r'^(?P<section>resources|snippets|tutorials|series)/create$',create,name="create"),
    url(r'^(?P<section>resources|snippets|tutorials|series)/(?P<display_type>all|latest|popular)/$',all,name="all"),
    url(r'^(?P<section>resources|snippets|tutorials)/(?P<slug>[\w-]+)/edit$',edit,name="edit"),
    url(r'^(?P<section>resources|snippets|tutorials)/(?P<slug>[\w-]+)/$',single,name="single"),
    url(r'^(?P<section>resources|snippets|tutorials|series)/(?P<slug>[\w-]+)/(?P<choice>upvote|downvote)/$',vote,name="vote"),
    url(r'^(?P<section>resources|snippets|tutorials|series)/$',all,{'display_type':'all'},name="default"),
    url(r'^series/(?P<slug_series>[\w-]+)/(?P<slug>[\w-]+)$',single,{'section':'seriestutorial'},name="single_seriestutorial"),
    url(r'^series/(?P<slug>[\w-]+)/$',single_series,name="single_series"),
    )