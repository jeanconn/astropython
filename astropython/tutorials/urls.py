from django.conf.urls import url

from .views import CreationWizard,FORMS

urlpatterns = [
    #url(r'^/home/', views.index, name='index'),
    #url(r'^/tutorials/', ),
    #url(r'^/resources/'),
    #url(r'^/snippets/'),
    url(r'^create/',CreationWizard.as_view(FORMS)),
]