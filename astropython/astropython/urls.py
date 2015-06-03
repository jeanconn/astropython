from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin

from moderation.helpers import auto_discover

admin.autodiscover()
auto_discover()# from moderation app -alway keep below admin.autodiscover()

urlpatterns = patterns('',
    url(r'^grappelli/', include('grappelli.urls')), #for admin urls
    url(r'^tinymce/', include('tinymce.urls')), #for tinymce urls
    url('', include('social.apps.django_app.urls', namespace='social')), #for social auth urls
    url(r'^admin/', include(admin.site.urls)), #additional admin urls
    url(r'^$', 'home.views.home', name='home'),#home url
    url(r'^roll/', 'home.views.roll', name='roll'),#Sample Templates
    url(r'^single/', 'home.views.single', name='single'),#Sample Templates
    url(r'',include('tutorials.urls')),#Teach and Learn
    #url(r'^blogs/', include('blog.urls')),
    #url(r'^packages/', include('packages.urls')),
)

#Access Static Files if in development
if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)