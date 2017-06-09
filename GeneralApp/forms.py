from django.contrib.auth.models import User
from django import forms
from django.conf import settings
from ProfileApp.models import Profile

class LoginForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)

	class Meta:
		model = Profile
		fields = ['username', 'password']
		
class UserForm(forms.Form):
	username1 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Pick a username'}))
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Create a password'}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm your password'}))
	email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your email address'}))

	class Meta:
		model = settings.AUTH_USER_MODEL
		fields = ['username1', 'password1', 'password2', 'email']