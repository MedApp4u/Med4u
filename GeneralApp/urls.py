from django.conf.urls import url

from . import views

app_name = 'GeneralApp'
urlpatterns = [
    url(r'login/', views.LoginFormView.as_view(), name='login'),
    url(r'registration/', views.UserFormView.as_view(), name='register'),
    url(r'tnc/', views.Tnc.as_view(), name='tnc'),
    url(r'about/', views.AboutUs.as_view(), name='about'),
    url(r'^accounts/profile/$', views.redirect_to_dashboard, name='redirect_to_dashboard'),
    # url(r'^reset-password/$', views.password_reset, {'template_name': 'GeneralApp/password_reset.html'},name='password_reset'),
    # url(r'^reset-password/done/$', views.password_reset_done, {'template_name': 'GeneralApp/password_reset_done.html'},name='password_reset_done'),
    # url(r'^reset-password/confirm/(?P<uidb36>[0-9A-Za-z]+)-(?P<key>.+)/$', views.password_reset_confirm, {'template_name': 'GeneralApp/password_reset_confirm.html'}),

]
