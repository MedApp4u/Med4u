# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import warnings

from django.contrib.auth import (
    REDIRECT_FIELD_NAME, get_user_model, login as auth_login,
    logout as auth_logout, update_session_auth_hash,
)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import (
    AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm,
)
from django.template.response import TemplateResponse
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.utils.deprecation import RemovedInDjango21Warning
from django.utils.http import is_safe_url, urlsafe_base64_decode
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.tokens import default_token_generator
from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from django.shortcuts import render
from .forms import LoginForm, UserForm
from django.template import loader
from django.views import generic
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.shortcuts import resolve_url
from django.views.decorators.cache import never_cache
from ProfileApp.models import Profile


# Create your views here.

class LoginFormView(View):
    form_class = LoginForm
    context = ""

    def get(self, request):
        form = self.form_class(None)
        context = ""
        return render(request, 'GeneralApp/login.html', {'form': form, 'context': context})

    def post(self, request):
        form = self.form_class(None)
        # cleaned (normalized) data

        context = ""
        username = request.POST['username']
        password = request.POST['password']

        # returns User objects if credentials are correct
        user = authenticate(username=username, password=password)

        if user is not None:

            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/dashboard')
            else:
                context = "User is banned"
        else:
            context = "Incorrect username or password"

        return render(request, 'GeneralApp/login.html', {'form': form, 'context': context})


class UserFormView(View):
    form_class = UserForm
    context = ""

    def get(self, request):
        form = self.form_class(None)
        context = ""
        return render(request, 'GeneralApp/registration.html', {'form': form, 'context': context})

    def post(self, request):
        form = self.form_class(request.POST)
        context = ""

        if form.is_valid():

            user = form.save(commit=False)

            # cleaned (normalized) data
            username1 = form.cleaned_data['username1']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            if password1 != password2:
                context = "Passwords do not match."
                return render(request, 'GeneralApp/registration.html', {'form': form, 'context': context})
            user.set_password(password1)
            user.save()

            # returns User objects if credentials are correct
            user = authenticate(username=username1, password=password1)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/dashboard')
                else:
                    context = "Existing user is banned."

        else:
            context = "Please select a unique username."

        return render(request, 'GeneralApp/registration.html', {'form': form, 'context': context})


'''def tnc(request):
    template = loader.get_template('GeneralApp/tnc.html')
    return HttpResponse(template.render(request))'''

def password_reset(request,
                   template_name='GeneralApp/password_reset.html',
                   email_template_name='GeneralApp/password_reset_email.html',
                   subject_template_name='GeneralApp/password_reset_subject.txt',
                   password_reset_form=PasswordResetForm,
                   token_generator=default_token_generator,
                   post_reset_redirect=None,
                   from_email=None,
                   extra_context=None,
                   html_email_template_name=None,
                   extra_email_context=None):
    warnings.warn("The password_reset() view is superseded by the "
                  "class-based PasswordResetView().",
                  RemovedInDjango21Warning, stacklevel=2)
    if post_reset_redirect is None:
        post_reset_redirect = reverse('GeneralApp:password_reset_done')
    else:
        post_reset_redirect = resolve_url(post_reset_redirect)

    if request.method == "POST":
        form = password_reset_form(request.POST)
        if form.is_valid():
            opts = {
                'use_https': request.is_secure(),
                'token_generator': token_generator,
                'from_email': from_email,
                'email_template_name': email_template_name,
                'subject_template_name': subject_template_name,
                'request': request,
                'html_email_template_name': html_email_template_name,
                'extra_email_context': extra_email_context,
            }
            form.save(**opts)
            return HttpResponseRedirect(post_reset_redirect)
    else:
        form = password_reset_form()
    context = {
        'form': form,
        'title': _('Password reset'),
    }
    if extra_context is not None:
        context.update(extra_context)

    return TemplateResponse(request, template_name, context)


def password_reset_done(request,
                        template_name='GeneralApp/password_reset_done.html',
                        extra_context=None):
    warnings.warn("The password_reset_done() view is superseded by the "
                  "class-based PasswordResetDoneView().",
                  RemovedInDjango21Warning, stacklevel=2)
    context = {
        'title': _('Password reset sent'),
    }
    if extra_context is not None:
        context.update(extra_context)

    return TemplateResponse(request, template_name, context)


# Doesn't need csrf_protect since no-one can guess the URL
@sensitive_post_parameters()
@never_cache
def password_reset_confirm(request, uidb64=None, token=None,
                           template_name='GeneralApp/password_reset_confirm.html',
                           token_generator=default_token_generator,
                           set_password_form=SetPasswordForm,
                           post_reset_redirect=None,
                           extra_context=None):
    """
    Check the hash in a password reset link and present a form for entering a
    new password.
    """
    warnings.warn("The password_reset_confirm() view is superseded by the "
                  "class-based PasswordResetConfirmView().",
                  RemovedInDjango21Warning, stacklevel=2)
    assert uidb64 is not None and token is not None  # checked by URLconf
    if post_reset_redirect is None:
        post_reset_redirect = reverse('GeneralApp:password_reset_complete')
    else:
        post_reset_redirect = resolve_url(post_reset_redirect)
    try:
        # urlsafe_base64_decode() decodes to bytestring
        uid = urlsafe_base64_decode(uidb64).decode()
        user = UserModel._default_manager.get(pk=uid)
    except (TypeError, ValueError, OverflowError, UserModel.DoesNotExist):
        user = None

    if user is not None and token_generator.check_token(user, token):
        validlink = True
        title = _('Enter new password')
        if request.method == 'POST':
            form = set_password_form(user, request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(post_reset_redirect)
        else:
            form = set_password_form(user)
    else:
        validlink = False
        form = None
        title = _('Password reset unsuccessful')
    context = {
        'form': form,
        'title': title,
        'validlink': validlink,
    }
    if extra_context is not None:
        context.update(extra_context)

    return TemplateResponse(request, template_name, context)




class Tnc(generic.TemplateView):
    template_name = 'GeneralApp/tnc.html'


class AboutUs(generic.TemplateView):
    template_name = 'GeneralApp/about.html'


def redirect_to_dashboard(request):
    return HttpResponseRedirect('/dashboard/')

