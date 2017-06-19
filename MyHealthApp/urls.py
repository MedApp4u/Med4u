from django.conf.urls import url

from . import views

app_name = 'MyHealthApp'
urlpatterns = [
    url(r'doctors_api/', views.Doctor_list.as_view(), name='doctors_api'),
    url(r'medicines_api/', views.Medicine_list.as_view(), name='medicines_api'),
    url(r'medicinenotes_api/', views.Medicine_Note_list, name='medicinenotes_api'),
    url(r'doctornotes_api/', views.Doctor_Note_list, name='doctornotes_api'),
    url(r'appointments_api/', views.Appointment_list, name='appointments_api'),
    url(r'symptoms_api/', views.Symptom_list, name='symptoms_api'),
    url(r'bodyparts_api/', views.Bodypart_list, name='bodyparts_api'),
    url(r'measurements_api/', views.Measurement_list, name='measurements_api'),
    url(r'insurances_api/', views.Insurance_list, name='insurances_api'),
    url(r'procedures_api/', views.Procedure_list, name='procedures_api'),
    url(r'view_insurance/', views.ViewInsurance, name='view_insurance'),
    url(r'^profile/(?P<pk>[0-9]+)/$',views.Profile_show.as_view()),
  
]

