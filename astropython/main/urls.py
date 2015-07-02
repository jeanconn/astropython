from django.conf.urls import patterns,url,include

from .models import *
from .views import *
from .feeds import *

urlpatterns = patterns('',
    url(r'^(?P<section>announcements|blog|education|events|news|packages|snippets|tutorials|wiki)/create$',create,name="create"),
    url(r'^(?P<section>announcements|blog|education|events|news|packages|snippets|tutorials|wiki)/create/(?P<slug>[\w-]+)$',create,name="create"),
    url(r'^(?P<section>announcements|blog|education|events|news|packages|snippets|tutorials|wiki)/(?P<slug>[\w-]+)/$',single,name="single"),
    url(r'^(?P<section>announcements|blog|education|events|news|packages|snippets|tutorials|wiki)/(?P<slug>[\w-]+)/(?P<choice>upvote|downvote)/$',vote,name="vote"),
    url(r'^(?P<section>announcements|blog|education|events|news|packages|snippets|tutorials|wiki)/$',all,name="all"),
    url(r'^user/posts$',written,name="user_posts"),
    url(r'^contact$',contact,name="contact"),
    url(r'^feeds/rss$',RSSFeed(),name="rss_feed"),
    #url(r'^feeds/atom$',ATOMFeed,name="atom_feed"),
    )