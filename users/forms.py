from django import forms

class UserRegistrationForm(forms.Form):
    fl_name = forms.CharField(label='First and Last Name', max_length=50)
    email = forms.CharField(label='Email', max_length=50)
    password = forms.CharField(label='Password', max_length=50)

class UserLoginForm(forms.Form):
    email = forms.CharField(label='Email', max_length=50)
    password = forms.CharField(label='Password', max_length=50)