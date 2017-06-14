from django.conf.urls import url

from . import views

app_name = 'GeneralApp'
urlpatterns = [
	url(r'^$', views.LoginFormView.as_view(), name='home'),
    url(r'login/', views.LoginFormView.as_view(), name='login'),
    url(r'registration/', views.UserFormView.as_view(), name='register'),
    url(r'dashboard/', views.dashboard, name='dashboard'),
    url(r'tnc/', views.Tnc.as_view(), name='tnc'),
    url(r'about/', views.AboutUs.as_view(), name='about'),
]
