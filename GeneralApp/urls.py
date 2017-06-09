from django.conf.urls import url

from . import views

app_name = 'GeneralApp'
urlpatterns = [
    url(r'login/', views.LoginFormView.as_view(), name='login'),
    url(r'tnc/', views.tnc, name='tnc'),    
    url(r'about/', views.AboutUs.as_view(), name='about'),
]
