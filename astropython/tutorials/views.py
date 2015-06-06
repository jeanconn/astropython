from django.shortcuts import render,HttpResponseRedirect,Http404
from django.core.paginator import Paginator

import random
from slugify import slugify
import datetime
import secretballot
from django.core.urlresolvers import reverse
from .forms import *
from .models import Tutorial,CodeSnippet,EducationalResource,TutorialSeries,SeriesTutorial

def get_model(name):
    if name=='resources':
        return EducationalResource
    elif name=='snippets':
        return CodeSnippet
    elif name=='tutorials':
        return Tutorial
    elif name=='series':
        return TutorialSeries
    else:
        return SeriesTutorial

def get_name(model):
    if model==Tutorial:
        return "Tutorials"
    elif model == CodeSnippet:
        return "Code Snippets"
    elif model== EducationalResource:
        return "Educational Resources"
    elif model== TutorialSeries:
        return "Tutorial Series"
    else:
        return "Tutorial for Series"

def user_check(user,obj_check):
    try:
        obj_check.authors.get(username=user.username)
    except:
        return False
    return True

def create(request,section):
    model=get_model(section)
    name =get_name(model)
    if request.method=='POST':
        kwargs ={'model':model}
        form = CustomForm(request.POST,**kwargs)
        instance=form.save(commit=False)
        instance.save()
        form.save_m2m()
        return HttpResponseRedirect(reverse('all',kwargs={'section':section,'display_type':'latest'}))
    return render(request,'tutorials/creation.html',{'form':CustomForm,'name':name,'btn':"Publish"})

"""
To view a single model instance
"""
def single(request,section,slug,**kwargs):
    model=get_model(section)
    #try:
    obj=model.objects.get(slug=slug)
    if(model != SeriesTutorial):
        obj.hits = obj.hits +1
    obj.save()
    context = {'obj':obj,'section':section}
    return render(request,'tutorials/single.html',context)
   # except:
        # Http404


def single_series(request,slug):
    series=TutorialSeries.objects.get(slug=slug)
    obj=series.seriestutorial_set.order_by('order_id')
    series.hits=series.hits+1
    series.save()
    context = {'obj':obj,'series':series,'name':series.title,'length':len(obj)}
    return render(request,'tutorials/single-series.html',context)


def vote(request,section,choice,slug):
    model=get_model(section)
    obj=model.objects.get(slug=slug)
    v=model.objects.from_request(request).get(pk=obj.pk)
    token=request.secretballot_token
    if(choice=='upvote'):
        t=1
    else:
        t=-1
    if v.user_vote==t:
        obj.remove_vote(token)
    else:
        obj.add_vote(token,t)
    return HttpResponseRedirect(reverse('single',kwargs={'slug':slug,'section':section}))

"""
General listing of all sections
"""

def all(request,section,display_type,**kwargs):
    model=get_model(section)
    name=get_name(model)
    if display_type=="all":
        obj_list=model.objects.all()
    elif display_type=="latest":
        obj_list=model.objects.all().order_by('-created')
    elif display_type=="popular":
        obj_list=model.objects.all().order_by('-hits')
    length=len(obj_list)
    paginator = Paginator(obj_list,15)
    page = request.GET.get('page')
    try:
        obj=paginator.page(page)
    except:
        obj=paginator.page(1)
    context = {'name':name,'obj':obj,'section':section,'length':length,'range':range(1,obj.paginator.num_pages+1)}
    return render(request,'tutorials/all.html',context)

"""
Editing of articles
"""

def edit(request,section,slug):
    model=get_model(section)
    name = get_name(model)
    pass