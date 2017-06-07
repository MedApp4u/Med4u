# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from django.shortcuts import render
from .forms import LoginForm
from django.template import loader

# Create your views here.

class LoginFormView(View):
	form_class = LoginForm
	context = ""

	def get(self, request):
		form = self.form_class(None)
		context = ""
		return render(request, 'HealthApp/login.html', {'form' : form, 'context': context})

	def post(self, request):
		form = self.form_class(None)
		#cleaned (normalized) data

		context = ""
		username = request.POST['username']
		password = request.POST['password']

		#returns User objects if credentials are correct
		user = authenticate(username=username, password=password)

		if user is not None:

			if user.is_active:
				login(request, user)
				return HttpResponse("Congrats! You are logged in!")
			else:
				context = "User is banned"
		else:
			context = "Incorrect username or password"

		return render(request, 'HealthApp/login.html', {'form': form, 'context': context})

def tnc(request):
    template = loader.get_template('HealthApp/tnc.html')
    return HttpResponse(template.render(request))
