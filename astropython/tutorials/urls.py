from django.conf.urls import patterns,url

from .views import create_tutorial,body_tutorial,finish_tutorial

urlpatterns = patterns('',
    url(r'^tutorials/create/$',create_tutorial,name="create_tutorial"),
    url(r'^tutorials/create/intermediate/(?P<slug>[\w-]+)/$',body_tutorial,name="body_tutorial"),
    url(r'^tutorials/create/finish/(?P<slug>[\w-]+)/$',finish_tutorial,name="finish_tutorial"),
    )