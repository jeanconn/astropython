from django.shortcuts import render,HttpResponseRedirect

import random
from slugify import slugify
import datetime

from django.core.urlresolvers import reverse
from .forms import HeaderForm,TailForm,WYSIWYGCodeBody,WYSIWYGTutorialBody,MarkdownCodeBody,MarkdownTutorialBody,WYSIWYGResourceBody,MarkdownResourceBody
from .models import Tutorial,CodeSnippet,EducationalResource,TutorialSeries,SeriesTutorial

name=""
def start_step(request,model,**kwargs):
    global name
    if(model==Tutorial):
        name="Tutorial"
    elif(model==CodeSnippet):
        name="Code Snippet"
    elif(model==EducationalResource):
        name="Educational Resource"
    elif(model==SeriesTutorial):
        name="Tutorial for Series"
        obj=TutorialSeries.objects.get(slug=kwargs['slug'])
    elif(model==TutorialSeries):
        name="Tutorial Series"
    if request.method == 'POST':
        form = HeaderForm(request.POST)
        if form.is_valid():
            model_instance = model()
            model_instance.title=form.cleaned_data['title']
            model_instance.abstract=form.cleaned_data['abstract']
            model_instance.input_type=form.cleaned_data['input_type']
            model_instance.slug=slugify(form.cleaned_data['title'])#Add acheck to see if slug is always unique
            if(model==SeriesTutorial):
                print TutorialSeries.objects.get(slug=kwargs['slug'])
                model_instance.tut_series=obj
            model_instance.save()
            model_instance.authors.add(request.user) #Add anonymous user config
            model_instance.save()
            url='creation_intermediate_'+(str(model.__name__)).lower()
            if(model==TutorialSeries):
                return HttpResponseRedirect(reverse('home'))
            elif(model==SeriesTutorial):
                return HttpResponseRedirect(reverse(url,kwargs={'slug':model_instance.slug,'slug_series':obj.slug}))
            else:
                return HttpResponseRedirect(reverse(url,kwargs={'slug':model_instance.slug}))

    return render(request,'tutorials/creation.html',{'form':HeaderForm,'name':name})

def intermediate_step(request,slug,model,**kwargs):
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
            url='creation_finish_'+(str(model.__name__)).lower()
            if(model==SeriesTutorial):
                return HttpResponseRedirect(reverse('home'))
            return HttpResponseRedirect(reverse(url,kwargs={'slug':obj.slug}))

    return render(request,'tutorials/creation.html',{'form':FormType,'name':name})

def finish_step(request,slug,model):
    obj=model.unmoderated_objects.get(slug=slug)
    if request.method=='POST':
        form = TailForm(request.POST,instance=obj)
        instance=form.save(commit=False)
        form.save_m2m()
        return HttpResponseRedirect(reverse('home'))
    return render(request,'tutorials/creation.html',{'form':TailForm,'name':name})
