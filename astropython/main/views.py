from django.shortcuts import render,HttpResponseRedirect,Http404,RequestContext
from django.contrib.auth import logout
from django.core.paginator import Paginator
from django.core.urlresolvers import reverse

from moderation.helpers import automoderate

import secretballot

from .forms import *
from .models import *
from .utilities import *

def home(request):
	template = 'index.html'
	context = locals()
	return render(request, template, context)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

def create(request,section,**kwargs):
    model=get_model(section)
    name =get_name(section)
    exclude_fields = get_exclude_fields(model)
    form = get_create_form(request,exclude_fields,model,kwargs)
    if request.method=="POST":
        state=set_state(request,form)
        if form.is_valid():
            instance=form.save(commit=False)
            slug = get_slug(request,model,instance.title,kwargs)
            user=get_user(request)
            instance.state=state
            instance.slug=slug
            instance.save()
            instance.authors.add(user)
            form.save_m2m()
            automoderate(instance,user)
            return render(request,'complete.html',{'section':section,'slug':slug,'state':state,'name':name})
    return render(request,'creation.html',{'form':form,'name':name})

"""
To view a single model instance
"""
def single(request,section,slug,**kwargs):
    model=get_model(section)
    obj=model.objects.get(slug=slug)
    obj.hits = obj.hits +1
    obj.save()
    mode="display"
    if not check_viewing_permission(request.user,obj):
        raise Http404
    if request.method=="GET" and 'edit' in request.GET:
            form= get_edit_form(request,model,obj)
            mode="edit"
    elif request.method=="POST":
        form = PostForm(model,request.session['edit_field'],'edit',request.POST,instance=obj)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.save()
            form.save_m2m()
            return HttpResponseRedirect(reverse('single',kwargs={'section':section,'slug':obj.slug}))
    else:
        form=None
    return render(request,'single.html',{'obj':obj,'section':section,'full_url':request.build_absolute_uri(),"mode":mode,"form":form})


def single_series(request,slug):
    series=TutorialSeries.objects.get(slug=slug)
    obj=series.seriestutorial_set.order_by('order_id')
    series.hits=series.hits+1
    series.save()
    context = {'obj':obj,'series':series,'name':series.title,'length':len(obj)}
    return render(request,'single-series.html',context)


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
    name=get_name(section)
    if display_type=="all":
        obj_list=model.objects.all().filter(state="submitted")
    elif display_type=="latest":
        obj_list=model.objects.all().filter(state="submitted").order_by('-created')
    elif display_type=="popular":
        obj_list=model.objects.all().filter(state="submitted").order_by('-hits')
    length=len(obj_list)
    paginator = Paginator(obj_list,15)
    page = request.GET.get('page')
    try:
        obj=paginator.page(page)
    except:
        obj=paginator.page(1)
    context = {'name':name,'obj':obj,'section':section,'length':length,'range':range(1,obj.paginator.num_pages+1)}
    return render(request,'all.html',context)