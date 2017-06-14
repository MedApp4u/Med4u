from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from django.shortcuts import render
from .forms import *
from django.template import loader
from django.views import generic
from django.contrib.auth.decorators import login_required 
# Create your views here.


class ViewProfile(View):
    form_class = ProfileForm
    context = ""

    def get(self, request):
        form = self.form_class(None)
        context = ""
        return render(request, 'view_profile.html', {'form': form, 'context': context})

    def post(self, request):
        form = self.form_class(request.POST)
        context = ""
        return render(request, 'view_profile.html', {'form': form, 'context': context})


        # if form.is_valid():

        #     user = form.save(commit=False)

        #     # cleaned (normalized) data
        #     username1 = form.cleaned_data['username1']
        #     password1 = form.cleaned_data['password1']
        #     password2 = form.cleaned_data['password2']
        #     if password1 != password2:
        #         context = "Passwords do not match."
        #         return render(request, 'GeneralApp/registration.html', {'form': form, 'context': context})
        #     user.set_password(password1)
        #     user.save()

        #     # returns User objects if credentials are correct
        #     user = authenticate(username=username1, password=password1)

        #     if user is not None:
        #         if user.is_active:
        #             login(request, user)
        #             return HttpResponse("User signed up succesfully!")
        #         else:
        #             context = "Existing user is banned."

        # else:
        #     context = "Please select a unique username."

        # return render(request, 'GeneralApp/registration.html', {'form': form, 'context': context})git 

@login_required
def LogoutProfile(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)
    # Take the user back to the homepage.
    return HttpResponseRedirect('/')