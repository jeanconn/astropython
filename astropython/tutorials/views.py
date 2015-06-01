from django.shortcuts import render,HttpResponseRedirect

import random
from slugify import slugify

from django.core.urlresolvers import reverse
from .forms import HeaderForm,WYSIWYGBodyForm,MarkdownBodyForm,TailForm
from .models import Tutorial

def create_tutorial(request):
    if request.method == 'POST':
        form = HeaderForm(request.POST)
        if form.is_valid():
            model_instance = Tutorial()
            model_instance.title=form.cleaned_data['title']
            model_instance.abstract=form.cleaned_data['abstract']
            model_instance.input_type=form.cleaned_data['input_type']
            model_instance.slug=slugify(form.cleaned_data['title'])#Add acheck to see if slug is always unique
            model_instance.save()
            model_instance.authors.add(request.user) #Add anonymous user config
            model_instance.save()
            return HttpResponseRedirect(reverse('body_tutorial',kwargs={'slug':model_instance.slug}))

    return render(request,'tutorials/create.html',{'form':HeaderForm})

def body_tutorial(request,slug):
    obj=Tutorial.unmoderated_objects.get(slug=slug)
    if (obj.input_type=="WYSIWYG"):
        FormType=WYSIWYGBodyForm
    else:
        FormType=MarkdownBodyForm
    if request.method == 'POST':
        if form.is_valid():
            obj.body = form.cleaned_data['body']
            obj.save()
            return HttpResponseRedirect(reverse('finish_tutorial',kwargs={'slug':obj.slug}))

    return render(request,'tutorials/create.html',{'form':FormType})

def finish_tutorial(request,slug):
    obj=Tutorial.unmoderated_objects.get(slug=slug)
    if request.method == 'POST':
        if form.is_valid():

    return render(request,'tutorials/create.html',{'form':TailForm})
