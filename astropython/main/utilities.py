from django.shortcuts import Http404
import random
from slugify import slugify

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

def get_section(model):
    if model==Tutorial:
        return 'tutorials'
    elif model==Snippet:
        return "snippets"
    elif model==EducationalResource:
        return "education"
    elif model==Wiki:
        return "wiki"
    elif model==Announcement:
        return "announcements"
    elif model==News:
        return "news"
    elif model==Blog:
        return "blog"
    elif model==Package:
        return "packages"
    elif model==Event:
        return "events"

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
        return "Blog Posts"
    elif name=="packages":
        return "Packages"
    elif name=="events":
        return "Events"

def get_exclude_fields(model):
    if model==Event:
        return ['slug','authors','state','hits']
    else:
        return ['slug','authors','state','hits']

def get_create_form(request,exclude_fields,model,kwargs):
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

def check_viewing_permission(user,obj):
    if(obj.state=="raw"):
        if not request.user in obj.authors.all():
            return False
    return True
def generate_temp_slug(model):
    slug="%0.12d" % random.randint(0,999999999999)
    while (model.objects.filter(slug=slug).exists() or model.unmoderated_objects.filter(slug=slug).exists()):
        slug="%0.12d" % random.randint(0,999999999999)
    return slug

def generate_final_slug(model,title):
    slug=slugify(title)
    while (model.objects.filter(slug=slug).exists() or model.unmoderated_objects.filter(slug=slug).exists()):
        slug=slug+str(random.randrange(1,1000+1))
    return slug

def get_slug(request,model,title,kwargs):
    if 'save' in request.POST:
        if 'slug' not in kwargs:
            return generate_temp_slug(model)
        else:
            return kwargs['slug']
    elif 'submit' in request.POST:
        return generate_final_slug(model,title)

def set_state(request,form):
    if 'submit' in request.POST:
        return "submitted"
    elif 'save' in request.POST:
        for field in form.fields:
            form.fields[field].required = False
        return "raw"

def get_user(request,):
    user=request.user
    if user.is_authenticated():
        return user
    else:
        u=User.objects.get_or_create(username="Anonymous")
        return u[0]