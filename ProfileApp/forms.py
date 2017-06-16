# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
	username=forms.CharField(max_length=30,required=True, widget=forms.TextInput(attrs={'class' : 'vp-form-field', 'id': ''}))
	first_name = forms.CharField(max_length=30, required=True)
	last_name = forms.CharField(max_length=30, required=True)
	email = forms.EmailField(max_length=254, help_text='Enter a valid email address only.')
	gender = forms.CharField(max_length=1, help_text='Enter M for Male and F for Female', label='Gender',required=True)
	dob=forms.DateField(required=True, label='Date of Birth')
	address=forms.CharField(required=False, label='Address')
	mobile_no=forms.IntegerField(required=False, max_value=9999999999, label='Mobile No.')
	blood_group=forms.CharField(required=False, label='Blood Group')

	class Meta:
		model=Profile
		fields=('username','first_name','last_name','gender','email','dob','address','mobile_no','blood_group',)

