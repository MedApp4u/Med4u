from django.conf.urls import include, url
from django.contrib import admin
from . import views
from django.contrib.auth.views import password_change,password_change_done,password_reset,password_reset_done,password_reset_confirm,password_reset_complete

app_name='ProfileApp'
urlpatterns = [
    # Examples:
    # url(r'^$', 'app.views.home', name='home'),
    # # url(r'^blog/', include('blog.urls')),
    # url(r'^login/$','app.views.loginuser',name='login'),
    # url(r'^accounts/login/$','app.views.loginuser',name='login'),
    # url(r'^register/$','app.views.register',name='register'),
    # url(r'^dashboard/$','app.views.dashboard',name='dashboard'),
    # url(r'^logout/$','app.views.logoutuser',name='logout'),
    # url(r'^reset_password/$',password_reset,name='reset_password'),
    # url(r'^change_password/$',password_change,name='password_change'),
    # url(r'^change_password/done$',password_change_done,name='password_change_done'),
    # url(r'^reset_password/done/$',password_reset_done,name='password_reset_done'),
    # url(r'^reset_password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',password_reset_confirm,name='password_reset_confirm'),
    # url(r'^reset_password/complete$',password_reset_complete,name='password_reset_complete'),
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^view_profile/$',views.ViewProfile.as_view(),name='view_profile'),
    url(r'^logout/$',views.ViewProfile,name='logout'),
]
