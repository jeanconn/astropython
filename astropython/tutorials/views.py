from django.shortcuts import render,HttpResponseRedirect,Http404

import random
from slugify import slugify
import datetime
import secretballot
from django.core.urlresolvers import reverse
from .forms import HeaderForm,TailForm,WYSIWYGCodeBody,WYSIWYGTutorialBody,MarkdownCodeBody,MarkdownTutorialBody,WYSIWYGResourceBody,MarkdownResourceBody
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

"""
Tutorial Creation Wizard comprises of 3 steps :
    The first step (or start_step) create the basic models and provides initial information to create the models , namely the title,abstract and preferred input mode
    The second step (or intermediate_step) fills up the rest of the information - body,extra info, etc
    The final step (or finish_step) adds the tags and categories to the model and will in the future include sharing on social network abilities
"""
name=""
def start_step(request,section,**kwargs):
    global name
    model=get_model(section)
    if(model==Tutorial):
        name="Tutorial"
    elif(model==CodeSnippet):
        name="Code Snippet"
    elif(model==EducationalResource):
        name="Educational Resource"
    elif(model==SeriesTutorial):
        name="Tutorial for Series"
        print kwargs['slug']
        obj=TutorialSeries.objects.get(slug=slugify(kwargs['slug']))
    elif(model==TutorialSeries):
        name="Tutorial Series"
    if request.method == 'POST':
        form = HeaderForm(request.POST)
        if form.is_valid():
            model_instance = model()
            model_instance.title=form.cleaned_data['title']
            model_instance.abstract=form.cleaned_data['abstract']
            model_instance.input_type=form.cleaned_data['input_type']
            model_instance.slug=slugify(form.cleaned_data['title'])#Add a check to see if slug is always unique
            if(model==SeriesTutorial):
                model_instance.tut_series=obj
            model_instance.save()
            model_instance.authors.add(request.user) #Add anonymous user config
            model_instance.save()
            if(model==TutorialSeries):
                return HttpResponseRedirect(reverse('home'))
            elif(model==SeriesTutorial):
                return HttpResponseRedirect(reverse('creation_intermediate_seriestutorial',kwargs={'slug':model_instance.slug,'slug_series':obj.slug}))
            else:
                return HttpResponseRedirect(reverse('creation_intermediate',kwargs={'slug':model_instance.slug,'section':section}))

    return render(request,'tutorials/creation.html',{'form':HeaderForm,'name':name})

def intermediate_step(request,slug,section,**kwargs):
    model=get_model(section)
    obj=model.unmoderated_objects.get(slug=slug)
    if (model==Tutorial or model==SeriesTutorial):
        if (obj.input_type=="WYSIWYG"):
            FormType=WYSIWYGTutorialBody
        else:
            FormType=MarkdownTutorialBody
    elif(model==CodeSnippet):
        if (obj.input_type=="WYSIWYG"):
            FormType=WYSIWYGCodeBody
        else:
            FormType=MarkdownCodeBody
    elif(model==EducationalResource):
        if (obj.input_type=="WYSIWYG"):
            FormType=WYSIWYGResourceBody
        else:
            FormType=MarkdownResourceBody
    if request.method == 'POST':
        form= FormType(request.POST)
        if form.is_valid():
            obj.body = form.cleaned_data['body']
            if (model==CodeSnippet):
                obj.snippet = form.cleaned_data['snippet']
            elif (model==EducationalResource):
                obj.start_date = datetime.datetime.strptime(form.cleaned_data['start_date'],"%Y-%m-%d")
                obj.instructor_names =form.cleaned_data['instructor_names']
                obj.website = form.cleaned_data['website']
                obj.background=form.cleaned_data['background']
                obj.language=form.cleaned_data['language']
            obj.save()
            url='creation_finish'
            if(model==SeriesTutorial):
                return HttpResponseRedirect(reverse('home'))
            return HttpResponseRedirect(reverse(url,kwargs={'slug':obj.slug,'section':section}))

    return render(request,'tutorials/creation.html',{'form':FormType,'name':name})

def finish_step(request,slug,section):
    model=get_model(section)
    obj=model.unmoderated_objects.get(slug=slug)
    if request.method=='POST':
        form = TailForm(request.POST,instance=obj)
        instance=form.save(commit=False)
        form.save_m2m()
        return HttpResponseRedirect(reverse('home'))
    return render(request,'tutorials/creation.html',{'form':TailForm,'name':name})

"""
To view a single model instance
"""
def single(request,section,slug,**kwargs):
    model=get_model(section)
    try:
        obj=model.objects.get(slug=slug)
        context = {'obj':obj}
        return render(request,'tutorials/single.html',context)
    except:
        raise Http404

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
