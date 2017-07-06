from django.conf.urls import url

from . import views

app_name = 'GeneralApp'
urlpatterns = [
    url(r'^login/$', views.LoginFormView.as_view(), name='login'),
    url(r'^registration/$', views.UserFormView.as_view(), name='register'),
    url(r'^tnc/$', views.Tnc.as_view(), name='tnc'),
    url(r'^about/$', views.AboutUs.as_view(), name='about'),
    url(r'^accounts/profile/$', views.redirect_to_dashboard, name='redirect_to_dashboard'),
    
    url(r'^symptoms/$', views.SymptomsView.as_view(), name='symptoms'),
    url(r'^symptom/head/$', views.SymptomHead,name='head-symptom'),
    url(r'^symptom/abdomen/$', views.SymptomAbdomen,name='abdomen-symptom'),
    url(r'^symptom/arms/$', views.SymptomArms,name='arms-symptom'),
    url(r'^symptom/chest/$', views.SymptomHead,name='chest-symptom'),
    url(r'^symptom/feet/$', views.SymptomHead,name='feet-symptom'),
    url(r'^symptom/hands/$', views.SymptomHead,name='hands-symptom'),
    url(r'^symptom/hips/$', views.SymptomHead,name='hips-symptom'),
    url(r'^symptom/legs/$', views.SymptomHead,name='legs-symptom'),
    url(r'^symptom/neck/$', views.SymptomHead,name='neck-symptom'),
    url(r'^symptom/pelvis/$', views.SymptomHead,name='pelvis-symptom'),
    url(r'^symptom/shoulder/$', views.SymptomShoulder,name='shoulder-symptom'),
    
    url(r'^procedures/$', views.procedures, name='procedures'),
    url(r'^procedures/(?P<proc_id>[0-9]+)$', views.procedure_details, name='procedure_details'),

    url(r'^doctors/$', views.doctors, name='doctors'),
    url(r'^doctors/doctors-find/$', views.doctors_map, name='doctors-map'),
    url(r'^doctors/(?P<doc_id>[0-9]+)$', views.doctor_details, name='doctor_details'),

    url(r'^medicines/$', views.medicines, name='medicines'),
    url(r'^medicines/(?P<med_id>[0-9]+)$', views.medicine_details, name='medicine_details'),

    url(r'^contacts/$', views.contacts, name='contacts'),
    url(r'^contacts/(?P<con_id>[0-9]+)$', views.contact_details, name='contact_details'),    

    url(r'^add_general_medicine/', views.AddGeneralMedicine, name='add_general_medicine'),    
    url(r'^add_general_doctor/', views.AddGeneralDoctor, name='add_general_doctor'),

    url(r'api/login/', views.Login_api.as_view(), name='login_api'),
    url(r'api/logout/', views.Logout_api, name='logout_api'),

]
