from django.shortcuts import render

# Create your views here.

def dashboard(request):
	template = 'dashboard.html'
	context = {
		'name': request.user.first_name.split(" ")[0]
	}
	return render(request, template, context)

def create(request):
	template = 'dashboard.html'
	return render(request, template)

def delete(request):
	template = 'dashboard.html'
	return render(request, template)

def toggle(request):
	template = 'dashboard.html'
	return render(request, template)