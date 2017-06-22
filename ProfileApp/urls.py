from django.conf.urls import include, url
from django.contrib import admin
from . import views
from django.contrib.auth.views import password_change,password_change_done,password_reset,password_reset_done,password_reset_confirm,password_reset_complete

app_name='ProfileApp'
urlpatterns = [
    url(r'^view_profile/$',views.ViewProfile,name='view_profile'),
    url(r'dashboard/', views.dashboard, name='dashboard'),
    url(r'^change_password/$',views.change_password,name='change_password'),
    url(r'^logout/$',views.LogoutProfile,name='logout'),
    # url(r'^api-token-auth/', views.obtain_auth_token),

]
