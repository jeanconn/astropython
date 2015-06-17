from django.conf.urls import patterns,url,include

from .models import *
from .views import *

urlpatterns = patterns('',
    url(r'^(?P<section>announcements|blog|education|events|news|packages|snippets|tutorials|wiki)/create$',create,name="create"),
    url(r'^(?P<section>announcements|blog|education|events|news|packages|snippets|tutorials|wiki)/create/(?P<slug>[\w-]+)$',create,name="create"),
    url(r'^(?P<section>announcements|blog|education|events|news|packages|snippets|tutorials|wiki)/(?P<slug>[\w-]+)/$',single,name="single"),
    url(r'^(?P<section>announcements|blog|education|events|news|packages|snippets|tutorials|wiki)/(?P<slug>[\w-]+)/(?P<choice>upvote|downvote)/$',vote,name="vote"),
    url(r'^(?P<section>announcements|blog|education|events|news|packages|snippets|tutorials|wiki)/$',all,name="all"),
    url(r'^series/(?P<slug_series>[\w-]+)/(?P<slug>[\w-]+)$',single,{'section':'seriestutorial'},name="single_seriestutorial"),
    url(r'^series/(?P<slug>[\w-]+)/$',single_series,name="single_series"),
    url(r'^user/posts$',written,name="user_posts"),
    )