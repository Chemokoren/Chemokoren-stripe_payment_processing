from django.shortcuts import render

# Create your views here.
def home(request):
	context ={}
	template ='home.html'
	return render(request,template,context)

# About Page.
def about(request):
	context ={}
	# context =locals()
	template ='about.html'
	return render(request,template,context)