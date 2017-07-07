from __future__ import unicode_literals
from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.views.generic import View
from django.template import loader
from django.views import generic
from django.contrib.auth.decorators import login_required 
from GeneralApp.forms import LoginForm
from .forms import *
from django.contrib.auth.forms import PasswordChangeForm
from .models import Profile
from rest_framework.decorators import api_view, renderer_classes
from .serializers import *
from ProfileApp.serializers import ProfileSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.renderers import JSONRenderer
# Create your views here.

@login_required
def ViewProfile(request):
    context = ""
    profile=Profile.objects.get(username=request.user.username)

    if request.method == 'GET':
        form = ProfileForm(instance=profile)
        return render(request, 'view_profile.html', {'form': form, 'context': context, 'current_user': request.user})

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES,instance=profile)
        context = ""
        form.save()
        return HttpResponseRedirect('/view_profile/')


@login_required
def LogoutProfile(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)
    # Take the user back to the homepage.
    return HttpResponseRedirect('/home')

@login_required
def dashboard(request):
    form_class = LoginForm
    form = form_class(None)
    
    current_user = request.user
    if not request.user.is_authenticated:
        context = "Please log in first."
        return render(request, 'GeneralApp/login.html', {'form': form, 'context': context})
        # return redirect('/')
    if request.user.get_username() == '':
        context = "Please log in first."
        return render(request, 'GeneralApp/login.html', {'context': context})
        # Context is not showing up, see if need to import views/urls in ProfileApp
    return render(request, 'dashboard.html', {'current_user': current_user})

@login_required
def change_password(request):
    current_user = request.user
    if request.method=='POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            return HttpResponseRedirect('/view_profile/')
        else:
            return HttpResponseRedirect('/change_password/')
    else:
        form=PasswordChangeForm(user=request.user)
        context={'form': form, 'current_user': current_user}
        return render(request,'change-password.html',context)

class Profile_register(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    renderer_classes = (JSONRenderer,)
