from django.conf.urls import url

from . import views

app_name = 'MyHealthApp'
urlpatterns = [
    url(r'^api/doctor_list/$', views.Doctor_list.as_view(), name='doctor_list'),
    url(r'^api/medicine_list/$', views.Medicine_list.as_view(), name='medicine_list'),
    url(r'^api/medicinenote_list/$', views.Medicine_Note_list.as_view(), name='medicinenote_list'),
    url(r'^api/doctornote_list/$', views.Doctor_Note_list.as_view(), name='doctornote_list'),
    url(r'^api/appointment_list/$', views.Appointment_list.as_view(), name='appointment_list'),
    url(r'^api/symptom_list/$', views.Symptom_list.as_view(), name='symptom_list'),
    url(r'^api/bodypart_list/$', views.Bodypart_list.as_view(), name='bodypart_list'),
    url(r'^api/measurement_list/$', views.Measurement_list.as_view(), name='measurement_list'),
    url(r'^api/insurance_list/$', views.Insurance_list.as_view(), name='insurance_list'),
    url(r'^api/procedure_list/$', views.Procedure_list.as_view(), name='procedure_list'),
    url(r'^api/disease_list/$', views.Disease_list.as_view(), name='disease_list'),

    url(r'^api/profile/(?P<pk>[0-9]+)/$', views.Profile_show.as_view(), name='Profile_show'),
    url(r'^api/doctor/(?P<pk>[0-9]+)/$', views.Doctor_show.as_view(), name='Doctor_show'),
    url(r'^api/medicine/(?P<pk>[0-9]+)/$', views.Medicine_show.as_view(), name='Medicine_show'),
    url(r'^api/disease/(?P<pk>[0-9]+)/$', views.Disease_show.as_view(), name='Disease_show'),
    url(r'^api/procedure/(?P<pk>[0-9]+)/$', views.Procedure_show.as_view(), name='Procedure_show'),
    url(r'^api/bodypart/(?P<pk>[0-9]+)/$', views.Bodypart_show.as_view(), name='Bodypart_show'),
    url(r'^api/symptom/(?P<pk>[0-9]+)/$', views.Symptom_show.as_view(), name='Symptom_show'),
  
    url(r'^home/$', views.HomeView.as_view(), name='home'),

    url(r'^MyHealth/$', views.MyHealthView.as_view(), name='MyHealth'),
    
    url(r'^my_medicines/$', views.MyMedicines, name='my_medicines'),
    url(r'^my_doctors/$', views.MyDoctors, name='my_doctors'),
    url(r'^my_appointments/$', views.MyAppointments, name='my_appointments'),
    url(r'^my_documents/$', views.MyDocuments, name='my_documents'),
    url(r'^my_diseases/$', views.MyDiseases, name='my_diseases'),
    url(r'^my_measurements/$', views.MyMeasurements, name='my_measurements'),
    url(r'^my_insurances/$', views.MyInsurances, name='my_insurance'),

    url(r'^add_insurance/$', views.AddInsurance, name='add_insurance'),
    url(r'^add_document/$', views.AddDocument, name='add_document'),
    url(r'^add_measurement/$', views.AddMeasurement, name='add_measurement'),
    url(r'^add_doctor/$', views.AddDoctor, name='add_doctor'),
    url(r'^add_appointment/$', views.AddAppointment, name='add_appointment'),
    url(r'^add_medicine/$', views.AddMedicine, name='add_medicine'),
    url(r'^add_disease/$', views.AddDisease, name='add_disease'),

    url(r'^my_insurances/(?P<ins_id>[0-9]+)/$', views.EditInsurance, name='edit_insurance'),
    url(r'^my_documents/(?P<docu_id>[0-9]+)/$', views.EditDocument, name='edit_document'),
    # url(r'^edit_measurement/$', views.EditMeasurement, name='edit_measurement'),
    url(r'^my_doctors/(?P<doc_id>[0-9]+)/$', views.EditDoctor, name='edit_doctor'),
    url(r'^my_appointments/(?P<app_id>[0-9]+)/$', views.EditAppointment, name='edit_appointment'),
    url(r'^my_medicines/(?P<med_id>[0-9]+)/$', views.EditMedicine, name='edit_medicine'),
    url(r'^my_diseases/(?P<dis_id>[0-9]+)/$', views.EditDisease, name='edit_disease'),

    url(r'^tokenapi/$', views.Tokenapi.as_view(), name='tokenapi'),

]
