import random
from slugify import slugify
import secretballot

from .forms import *
from .models import *

def get_model(name):
    if name=='tutorials':
        return Tutorial
    elif name=="snippets":
        return Snippet
    elif name=="education":
        return EducationalResource
    elif name=="wiki":
        return Wiki
    elif name=="announcements":
        return Announcement
    elif name=="news":
        return News
    elif name=="blog":
        return Blog
    elif name=="packages":
        return Package
    elif name=="events":
        return Event

def get_name(name):
    if name=='tutorials':
        return "Tutorials"
    elif name=="snippets":
        return "Code Snippets"
    elif name=="education":
        return "Educational Resources"
    elif name=="wiki":
        return "Wiki Pages"
    elif name=="announcements":
        return "Announcements"
    elif name=="news":
        return "News Articles"
    elif name=="blog":
        return "BLog Posts"
    elif name=="packages":
        return "Packages"
    elif name=="events":
        return "Events"

def get_exclude_fields(model):
    if model==Event:
        return ['slug','authors','state','hits','attendee']
    else:
        return ['slug','authors','state','hits']

def get_form(request,exclude_fields,model,kwargs):
    if 'slug' in kwargs:
        obj=model.objects.get(slug=kwargs['slug'])
        if check_editing_permission(request.user,obj):
            return PostForm(model,exclude_fields,'create',request.POST or None,instance=obj)
        else:
            raise Http404
    return PostForm(model,exclude_fields,'create',request.POST or None)


def check_editing_permission(user,obj):
    if ((not user in obj.authors.all()) or (obj.state=="submitted") ):
        return False
    return True

def save_instance():
    pass