from django.contrib.auth.models import User
from django import forms

class LoginForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ['username', 'password']
		
class UserForm(forms.ModelForm):
	username1 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Pick a username'}))
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Create a password'}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm your password'}))
	email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your email address'}))

	class Meta:
		model = User
		fields = ['username1', 'password1', 'password2', 'email']