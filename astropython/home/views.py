from django.shortcuts import render

# Create your views here.

def home(request):
	template = 'index.html'
	context = locals()
	return render(request, template, context)
