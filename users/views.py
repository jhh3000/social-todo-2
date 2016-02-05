from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from .forms import UserLoginForm, UserRegistrationForm

# Create your views here.

def home(request):
	if request.user.is_authenticated():
		return redirect(reverse('dashboard'))
	template = 'home.html'
	return render(request, template)

def dashboard(request):
	template = 'dashboard.html'
	return render(request, template)

def web_login(request):
	template = 'home.html'
	if request.method == 'POST':
		email = request.POST['email']
		if User.objects.filter(username=email).count() == 0:
			return render(request, template, {'login_error': "Invalid email address"})

		password = request.POST['password']
		user = authenticate(username=email, password=password)
		if user is not None:
			login(request, user)
			return redirect(reverse('dashboard'))
		else:
			return render(request, template, {'login_error': "Invalid password"})
	return redirect(reverse('home'))

def web_logout(request):
	logout(request)
	return redirect(reverse('home'))

def register(request):
	template = 'home.html'
	if request.method == 'POST':
		form = UserRegistrationForm(request.POST)
		if form.is_valid():
			email = form.cleaned_data['email']
			password = form.cleaned_data['password']
			fl_name = form.cleaned_data['fl_name']
			if User.objects.filter(username=email).count() > 0:
				return render(request, template, {'registration_error': "Account with this email already exists!"})

			user = User.objects.create_user(email, password=password)
			user.first_name = fl_name
			user.save()
			return web_login(request)
		else:
			login_form = UserLoginForm()
	return render(request, template, {'form': form})
