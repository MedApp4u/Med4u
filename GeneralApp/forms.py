from django import forms
from django.conf import settings
from ProfileApp.models import Profile
from MyHealthApp.models import Procedure, Symptom, Bodypart
from MyHealthApp.choices import *
from django.contrib.auth.forms import PasswordResetForm
from django.forms import inlineformset_factory
from GeneralApp.choices import *


FIELD_NAME_MAPPING = {
	'username': 'username1',
	'password1': 'password1',
	'password2': 'password2',
	'email': 'email'
}

class LoginForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)

	class Meta:
		model = Profile
		fields = ['username', 'password']
		
class UserForm(forms.ModelForm):

	def add_prefix(self, field_name):
        # look up field name; return original if not found
		field_name = FIELD_NAME_MAPPING.get(field_name, field_name)
		return super(UserForm, self).add_prefix(field_name)

	username1 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Pick a username'}))
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Create a password'}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm your password'}))
	email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your email address'}))

	class Meta:
		model = Profile
		fields = ['username', 'password1', 'password2', 'email']

class MyPasswordResetForm(PasswordResetForm):
	email = forms.EmailField(widget=forms.TextInput(attrs={'class' : 'rp-form-field', 'id': 'rp-form-field-email'}))

class ProcedureForm(forms.ModelForm):
	bodypart = forms.ChoiceField(choices=BODYPART,required=False, label='Procedure-Bodypart',initial='Select', widget=forms.Select(attrs={'class': 'procedure-form-field', 'id': 'procedure-form-bodypart', 'onchange': 'this.form.submit()'}))
	# queryset = Symptom.objects.all()
	symptom = forms.ChoiceField(choices=SYMPTOMS, required=False, label='Procedure-Symptom',initial='Select', widget=forms.Select(attrs={'class': 'procedure-form-field', 'id': 'procedure-form-symptom'}))
	# SymptomFormSet = inlineformset_factory(Bodypart, Symptom, )

	class Meta:
		model = Procedure
		fields = ['procedure_name', 'procedure_description', 'possible_complication', 'bodypart', 'symptom', 'medicine', 'doctor']