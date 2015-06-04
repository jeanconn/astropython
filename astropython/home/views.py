from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth import logout
from django.core.urlresolvers import reverse
# Create your views here.

def home(request):
	template = 'index.html'
	context = locals()
	return render(request, template, context)


def single(request):
	template = 'tutorials/single.html'
	context = locals()
	return render(request, template, context)

def roll(request):
	template = 'tutorials/roll.html'
	context = locals()
	return render(request, template, context)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))