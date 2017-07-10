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
    url(r'^api/mydoctors/(?P<id1>[0-9]+)/$', views.MyDoctorsapi.as_view(), name='MyDoctorsapi'),
    url(r'^api/mydoctornotes/(?P<id1>[0-9]+)/(?P<id2>[0-9]+)/$', views.MyDoctorNotesapi.as_view(), name='MyDoctorNotesapi'),

    url(r'^api/mymedicines/(?P<id1>[0-9]+)/$', views.MyMedicineapi.as_view(), name='MyMedicineapi'),
    url(r'^api/mymedicinenotes/(?P<id1>[0-9]+)/(?P<id2>[0-9]+)/$', views.MyMedicineNotesapi.as_view(), name='MyMedicineNotesapi'),
    url(r'^api/mydiseases/(?P<id1>[0-9]+)/$', views.MyDiseasesapi.as_view(), name='MyDiseasesapi'),
    url(r'^api/mydiseasenotes/(?P<id1>[0-9]+)/(?P<id2>[0-9]+)/$', views.MyDiseaseNotesapi.as_view(), name='MyDiseaseNotesapi'),
    # url(r'^api/myprocedures/(?P<id1>[0-9]+)/$', views.MyProceduresapi.as_view(), name='MyProceduresapi'),
    # url(r'^api/bodypart/(?P<pk>[0-9]+)/$', views.Bodypart_show.as_view(), name='Bodypart_show'),
    # url(r'^api/mysymptoms/(?P<pk>[0-9]+)/$', views.MySymptomsapi.as_view(), name='Symptom_show'),
    url(r'^api/myappointments/(?P<id1>[0-9]+)/$', views.MyAppointmentsapi.as_view(), name='MyAppointmentsapi'),
    url(r'^api/myinsurances/(?P<id1>[0-9]+)/$', views.MyInsurancesapi.as_view(), name='MyInsurancesapi'),
    url(r'^api/mymeasurements/(?P<id1>[0-9]+)/$', views.MyMeasurementsapi.as_view(), name='MyMeasurementsapi'),


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
    url(r'^my_doctors/(?P<doc_id>[0-9]+)/$', views.EditDoctor, name='edit_doctor'),
    url(r'^my_appointments/(?P<app_id>[0-9]+)/$', views.EditAppointment, name='edit_appointment'),
    url(r'^my_medicines/(?P<med_id>[0-9]+)/$', views.EditMedicine, name='edit_medicine'),
    url(r'^my_diseases/(?P<dis_id>[0-9]+)/$', views.EditDisease, name='edit_disease'),
    url(r'^my_measurements/(?P<mes_id>[0-9]+)/$', views.EditMeasurement, name='edit_measurement'),
  
    url(r'^delete_insurance/(?P<ins_id>[0-9]+)/$', views.DeleteInsurance, name='delete_insurance'),
    url(r'^delete_document/(?P<docu_id>[0-9]+)/$', views.DeleteDocument, name='delete_document'),
    url(r'^delete_doctor/(?P<doc_id>[0-9]+)/$', views.DeleteDoctor, name='delete_doctor'),
    url(r'^delete_appointment/(?P<app_id>[0-9]+)/$', views.DeleteAppointment, name='delete_appointment'),
    url(r'^delete_medicine/(?P<med_id>[0-9]+)/$', views.DeleteMedicine, name='delete_medicine'),
    url(r'^delete_disease/(?P<dis_id>[0-9]+)/$', views.DeleteDisease, name='delete_disease'),
    url(r'^delete_measurement/(?P<mes_id>[0-9]+)/$', views.DeleteMeasurement, name='delete_measurement'),

]
