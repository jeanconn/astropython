from django.conf.urls import patterns,url,include

from .models import Tutorial,CodeSnippet,EducationalResource,TutorialSeries,SeriesTutorial
from .views import start_step,intermediate_step,finish_step,single,vote,all,single_series

urlpatterns = patterns('',
    url(r'^(?P<section>resources|snippets|tutorials|series)/create$',start_step,name="creation_start"),
    url(r'^(?P<section>resources|snippets|tutorials)/create/intermediate/(?P<slug>[\w-]+)/$',intermediate_step,name="creation_intermediate"),
    url(r'^(?P<section>resources|snippets|tutorials|series)/create/finish/(?P<slug>[\w-]+)/$',finish_step,name="creation_finish"),
    url(r'^(?P<section>resources|snippets|tutorials|series)/(?P<display_type>all|latest|popular)/$',all,name="all"),
    url(r'^(?P<section>resources|snippets|tutorials)/(?P<slug>[\w-]+)/$',single,name="single"),
    url(r'^(?P<section>resources|snippets|tutorials|series)/(?P<slug>[\w-]+)/(?P<choice>upvote|downvote)/$',vote,name="vote"),
    url(r'^(?P<section>resources|snippets|tutorials|series)/$',all,{'display_type':'all'},name="default"),
    url(r'^series/(?P<slug>[\w-]+)/create$',start_step,{'section':'seriestutorial'},name="creation_start_seriestutorial"),
    url(r'^series/(?P<slug_series>[\w-]+)/add/(?P<slug>[\w-]+)/complete$',intermediate_step,{'section':'seriestutorial'},name="creation_intermediate_seriestutorial"),
    url(r'^series/(?P<slug_series>[\w-]+)/(?P<slug>[\w-]+)$',single,{'section':'seriestutorial'},name="single_seriestutorial"),
    url(r'^series/(?P<slug>[\w-]+)/$',single_series,name="single_series"),
    )