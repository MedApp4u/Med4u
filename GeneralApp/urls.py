from django.conf.urls import url

from . import views

app_name = 'HealthApp'
urlpatterns = [
    url(r'login/', views.LoginFormView.as_view(), name='login'),
    url(r'tnc/', views.tnc, name='tnc'),    
]
