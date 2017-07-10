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
    url(r'^symptoms/(?P<symptom_part>[\w.@+-]+)/$', views.BodypartSymptomList, name='symptom_part'),
    
    url(r'^procedures/$', views.procedures, name='procedures'),
    url(r'^procedures/(?P<proc_id>[0-9]+)$', views.procedure_details, name='procedure_details'),

    url(r'^doctors/$', views.doctors, name='doctors'),
    url(r'^doctors/doctors-find/$', views.doctors_map, name='doctors-map'),
    url(r'^doctors/(?P<doc_id>[0-9]+)$', views.doctor_details, name='doctor_details'),

    url(r'^medicines/$', views.medicines, name='medicines'),
    url(r'^medicines/(?P<med_id>[0-9]+)$', views.medicine_details, name='medicine_details'),

    url(r'^diseases/$', views.diseases, name='diseases'),
    url(r'^diseases/(?P<dis_id>[0-9]+)$', views.disease_details, name='disease_details'),

    url(r'^contacts/$', views.contacts, name='contacts'),
    url(r'^contacts/(?P<con_id>[0-9]+)$', views.contact_details, name='contact_details'),    

    url(r'^add_general_medicine/', views.AddGeneralMedicine, name='add_general_medicine'),    
    url(r'^add_general_doctor/', views.AddGeneralDoctor, name='add_general_doctor'),
    url(r'^add_general_disease/', views.AddGeneralDisease, name='add_general_disease'),

    url(r'api/login/', views.Login_api.as_view(), name='login_api'),
    url(r'api/logout/', views.Logout_api, name='logout_api'),

]
