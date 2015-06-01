from django.conf.urls import url

from . import views

urlpatterns = [
    #url(r'^/home/', views.index, name='index'),
    #url(r'^/tutorials/', ),
    #url(r'^/resources/'),
    #url(r'^/snippets/'),
    url(r'^create/','home.views.roll', name='tlroll')
]