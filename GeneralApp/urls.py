from django.conf.urls import url

from . import views

app_name = 'GeneralApp'
urlpatterns = [
    url(r'login/', views.LoginFormView.as_view(), name='login'),
    url(r'registration/', views.UserFormView.as_view(), name='register'),
    url(r'tnc/', views.Tnc.as_view(), name='tnc'),
    url(r'about/', views.AboutUs.as_view(), name='about'),
    url(r'^accounts/profile/$', views.redirect_to_dashboard, name='redirect_to_dashboard'),
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
    # url(r'^procedures/test$', views.procedures_test, name='procedures-test'),
]
