from django.shortcuts import render

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