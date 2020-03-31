from django.shortcuts import render

# Create your views here.
def home(request):
	context =locals()
	template ='home.html'
	return render(request,template,context)

# About Page.
def about(request):
	context =locals()
	template ='about.html'
	return render(request,template,context)