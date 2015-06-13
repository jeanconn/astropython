from django.conf.urls import patterns,url,include

from .models import Tutorial,CodeSnippet,EducationalResource,TutorialSeries,SeriesTutorial
from .views import create,single,vote,all,single_series

urlpatterns = patterns('',
    url(r'^(?P<section>resources|snippets|tutorials|wiki)/create$',create,name="create"),
    url(r'^(?P<section>resources|snippets|tutorials|wiki)/create/(?P<slug>[\w-]+)$',create,name="create"),
    url(r'^(?P<section>resources|snippets|tutorials|wiki)/(?P<display_type>all|latest|popular)/$',all,name="all"),
    url(r'^(?P<section>resources|snippets|tutorials|wiki)/(?P<slug>[\w-]+)/$',single,name="single"),
    url(r'^(?P<section>resources|snippets|tutorials|wiki)/(?P<slug>[\w-]+)/(?P<choice>upvote|downvote)/$',vote,name="vote"),
    url(r'^(?P<section>resources|snippets|tutorials|wiki)/$',all,{'display_type':'all'},name="default"),
    url(r'^series/(?P<slug_series>[\w-]+)/(?P<slug>[\w-]+)$',single,{'section':'seriestutorial'},name="single_seriestutorial"),
    url(r'^series/(?P<slug>[\w-]+)/$',single_series,name="single_series"),
    )