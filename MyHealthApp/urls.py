from django.conf.urls import url

from . import views

app_name = 'MyHealthApp'
urlpatterns = [
    url(r'doctors_api/', views.Doctor_list.as_view(), name='doctors_api'),
    url(r'medicines_api/', views.Medicine_list.as_view(), name='medicines_api'),
    url(r'medicinenotes_api/', views.Medicine_Note_list.as_view(), name='medicinenotes_api'),
    url(r'doctornotes_api/', views.Doctor_Note_list.as_view(), name='doctornotes_api'),
    url(r'appointments_api/', views.Appointment_list.as_view(), name='appointments_api'),
    url(r'symptoms_api/', views.Symptom_list.as_view(), name='symptoms_api'),
    url(r'bodyparts_api/', views.Bodypart_list.as_view(), name='bodyparts_api'),
    url(r'measurements_api/', views.Measurement_list.as_view(), name='measurements_api'),
    url(r'insurances_api/', views.Insurance_list.as_view(), name='insurances_api'),
    url(r'procedures_api/', views.Procedure_list.as_view(), name='procedures_api'),
    url(r'view_insurance/', views.ViewInsurance, name='view_insurance'),
    url(r'^profileapi/(?P<pk>[0-9]+)/$', views.Profile_show.as_view(), name='Profile_show'),
    url(r'^doctorapi/(?P<pk>[0-9]+)/$', views.Doctor_show.as_view(), name='Doctor_show'),
    url(r'^medicineapi/(?P<pk>[0-9]+)/$', views.Medicine_show.as_view(), name='Medicine_show'),
    url(r'^diseaseapi/(?P<pk>[0-9]+)/$', views.Disease_show.as_view(), name='Disease_show'),
    url(r'^procedureapi/(?P<pk>[0-9]+)/$', views.Procedure_show.as_view(), name='Procedure_show'),
    url(r'^bodypartapi/(?P<pk>[0-9]+)/$', views.Bodypart_show.as_view(), name='Bodypart_show'),
    url(r'^Symptomapi/(?P<pk>[0-9]+)/$', views.Symptom_show.as_view(), name='Symptom_show'),
    url(r'home/', views.HomeView.as_view(), name='home'),
    url(r'symptoms/', views.SymptomsView.as_view(), name='symptoms'),
    url(r'MyHealth/', views.MyHealthView.as_view(), name='MyHealth'),
    url(r'sidebar/', views.sidebarView.as_view(), name='sidebar'),
	  url(r'my_medicines/', views.medicinesView.as_view(), name='medicines'),
    url(r'my_doctors/', views.doctorsView.as_view(), name='doctors'),
    url(r'my_appointments/', views.appointmentsView.as_view(), name='appointments'),
    url(r'my_documents/', views.documentsView.as_view(), name='documents'),
    url(r'my_diseases/', views.diseasesView.as_view(), name='diseases'),
    url(r'my_measurements/', views.measurementsView.as_view(), name='measurements'),
    url(r'my_insurance/', views.insuranceView.as_view(), name='insurance'),
  
  
]
