from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

from .forms import UserLoginForm, UserRegistrationForm

# Create your views here.

def home(request):
	if request.method == 'POST':
		if request.POST['action'] == 'login':
			login_form = UserLoginForm(request.POST)
			if login_form.is_valid():
				email = login_form.cleaned_data['email']
				password = login_form.cleaned_data['password']

				user = Users.objects.get(email=email)
				login(request, user)
				return redirect(reverse('dashboard'))
			else:
				registration_form = UserRegistrationForm()

		if request.POST['action'] == 'register':
			registration_form = UserRegistrationForm(request.POST)
			if registration_form.is_valid():
				email = registration_form.cleaned_data['email']
				password = registration_form.cleaned_data['password']
				fl_name = registration_form.cleaned_data['fl_name']

				user = User.objects.create_user(email, password=password)
				user.first_name = fl_name
				user.save()
				return redirect(reverse('dashboard'))
			else:
				login_form = UserLoginForm()
	else:
		login_form = UserLoginForm()
		registration_form = UserRegistrationForm()

	template = 'home.html'
	return render(request, template, {'login_form': login_form, 'registration_form': registration_form})

def dashboard(request):
	template = 'dashboard.html'
	return render(request, template)

def login(request):
	return redirect(reverse('home'))

def logout(request):
	return redirect(reverse('home'))

def register(request):
	return redirect(reverse('home'))