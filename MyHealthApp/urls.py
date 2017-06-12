from django.conf.urls import url

from . import views

app_name = 'MyHealthApp'
urlpatterns = [
    url(r'doctors_api/', views.Doctor_list, name='doctors_api'),
    url(r'medicines_api/', views.Medicine_list, name='medicines_api'),
]
