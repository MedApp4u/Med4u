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

# Create your views here.

# #profile page using user name as url
# @login_required
# def profile_page(request, username):
#     user = get_object_or_404(User, username=username)
#     return render(request, 'howdidu/profile.html', {'profile_user': user})
# def get_user_profile(request, username):
#     user = User.objects.get(username=username)
#     return render(request, '<app_name>/user_profile.html', {"user":user})


# def bound_form(request, id):
#     item = get_object_or_404(Item, id=id)
#     form = ItemForm(instance=item)
#     return render_to_response('bounded_form.html', {'form': form})


# class ViewProfile(View):
#     context = ""
    
#     def get(self, request):
#         user = Profile.objects.get(user=request.user)
#         context = ""
#         return render(request, 'view_profile.html', {'user': user, 'context': context})

#     def post(self, request):
#         context = ""
#         return render(request, 'view_profile.html', {'user': user, 'context': context})


# #user profile form
# @login_required
# def register_profile(request):
#     profile = UserProfile.objects.get(user=request.user)
#     if request.method == 'POST':
#         form = UserProfileForm(request.POST, request.FILES, instance=profile)
#         if form.is_valid():
#             form.save()
#             return index(request)
#         else:
#             print form.errors
#     else:
#         form = UserProfileForm()
#     return render(request, 'howdidu/register_profile.html', {'form': form})

@login_required
def ViewProfile(request):
    context = ""
    profile=Profile.objects.get(username=request.user.username)

    if request.method == 'GET':
        form = ProfileForm(instance=profile)
        return render(request, 'view_profile.html', {'form': form, 'context': context, 'current_user': request.user})

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        context = ""
        form.save()
        return HttpResponseRedirect('/view_profile/')


# @login_required
# def EditProfile(request):
   
# class EditProfile(View):
#     context = ""
#     form_class = ProfileForm

#     def get(self, request):
#         profile=Profile.objects.get(user=request.user)
#         form = self.form_class(None)
#         context = ""
#         return render(request, 'edit_profile.html', {'form': form, 'context': context})

#     def post(self, request):
#         profile=Profile.objects.get(user=request.user)
#         form = self.form_class(request.POST)
#         context = ""
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/view_profile/')
#         else:
#             print form.errors
#         return render(request, 'edit_profile.html', {'form': form, 'context': context})

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
