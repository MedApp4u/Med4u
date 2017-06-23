"""DjangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, password_reset_complete
from MyHealthApp import views
from GeneralApp.forms import MyPasswordResetForm
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    url(r'^', include('GeneralApp.urls', namespace="GeneralApp")), 
    url(r'^', include('MyHealthApp.urls', namespace="MyHealthApp")), 
    url(r'^', include('ProfileApp.urls', namespace="ProfileApp")), 
    # url(r'^settings/$', core_views.settings, name='settings'),
    # url(r'^settings/password/$', core_views.password, name='password'),
    url(r'^reset_password/$',password_reset, {'template_name': 'GeneralApp/password_reset.html', 'password_reset_form': MyPasswordResetForm}, name='reset_password'),
    url(r'^reset_password/done/$',password_reset_done, {'template_name': 'GeneralApp/password_reset_done.html'}, name='password_reset_done'),
    url(r'^reset_password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',password_reset_confirm, {'template_name': 'GeneralApp/password_reset_confirm.html'}, name='password_reset_confirm'),
    url(r'^reset_password/complete$',password_reset_complete,  {'template_name': 'GeneralApp/password_reset_complete.html'}, name='password_reset_complete'),
    url(r'^home/$', views.HomeView, name='home'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)