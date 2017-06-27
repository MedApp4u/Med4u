# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from .models import *
from django import forms

class DocumentForm(forms.ModelForm):
	doc=forms.ImageField(required=False, label='Upload Document')
	notes=forms.CharField(required=False, label='Notes', widget=forms.Textarea())

	class Meta:
		model=Document
		fields = ('doc','notes')