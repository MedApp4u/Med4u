from __future__ import unicode_literals
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.views.generic import View
from django.template import loader
from django.views import generic
from django.contrib.auth.decorators import login_required 
from GeneralApp.forms import LoginForm
from .forms import *
from django.contrib.auth.forms import PasswordChangeForm
from .models import

# Create your views here.

# #profile page using user name as url
# @login_required
# def profile_page(request, username):
#     user = get_object_or_404(User, username=username)
#     return render(request, 'howdidu/profile.html', {'profile_user': user})
# def get_user_profile(request, username):
#     user = User.objects.get(username=username)
#     return render(request, '<app_name>/user_profile.html', {"user":user})

@login_required
class ViewProfile(View):
    context = ""
    user = Profile.objects.get(user=request.user)

    def get(self, request):
        context = ""
        return render(request, 'view_profile.html', {'user': user, 'context': context})

    def post(self, request):
        context = ""
        return render(request, 'view_profile.html', {'user': user, 'context': context})


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
class EditProfile(View):
    profile=Profile.objects.get(user=request.user)
    context = ""

    def get(self, request):
        form = self.form_class(None)
        context = ""
        return render(request, 'edit_profile.html', {'form': form, 'context': context})

    def post(self, request):
        form = ProfileForm(request.POST)
        context = ""
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/view_profile/')
        else:
            print form.errors
        return render(request, 'edit_profile.html', {'form': form, 'context': context})

@login_required
def LogoutProfile(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)
    # Take the user back to the homepage.
    return HttpResponseRedirect('/')

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
