from django.conf.urls import url

from . import views

app_name = 'GeneralApp'
urlpatterns = [
    url(r'login/', views.LoginFormView.as_view(), name='login'),
    url(r'registration/', views.UserFormView.as_view(), name='register'),
    url(r'tnc/', views.Tnc.as_view(), name='tnc'),
    url(r'about/', views.AboutUs.as_view(), name='about'),
    url(r'^accounts/profile/$', views.redirect_to_dashboard, name='redirect_to_dashboard'),
    url(r'^procedures/$', views.procedures, name='procedures'),
]
