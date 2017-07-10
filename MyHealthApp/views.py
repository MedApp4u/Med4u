from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from rest_framework import status
from .models import Measurement, Doctor, Doctor_Note, Medicine_Note, Medicine, Bodypart, Appointment, Symptom, \
    Insurance, Procedure
from django.contrib.auth.decorators import login_required
# from .serializers import DoctorSerializer,Doctor_NoteSerializer,Medicine_NoteSerializer,MedicineSerializer,MeasurementSerializer, BodypartSerializer, SymptomSerializer , InsuranceSerializer, ProcedureSerializer, AppointmentSerializer
from .serializers import *
from .forms import *
from rest_framework.views import APIView
from ProfileApp.models import Profile
from ProfileApp.serializers import ProfileSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework import generics
from django.views import generic
from rest_framework.authtoken.models import Token
from rest_framework.renderers import JSONRenderer
from django.shortcuts import get_object_or_404


# Create your views here

class Doctor_list(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('id',)
    search_fields = ('doctor_name',)
    renderer_classes = (JSONRenderer,)

    def perform_create(self, serializer):
        doctor = serializer.save(owner=self.request.user)
        doctor.user.add(self.request.user)


class Medicine_list(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('user',)
    search_fields = ('medicine_name',)
    renderer_classes = (JSONRenderer,)


class Disease_list(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    queryset = Disease.objects.all()
    serializer_class = DiseaseSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('id',)
    search_fields = ('Disease_name',)
    renderer_classes = (JSONRenderer,)


class Appointment_list(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('id',)
    renderer_classes = (JSONRenderer,)


class Symptom_list(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    queryset = Symptom.objects.all()
    serializer_class = SymptomSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    renderer_classes = (JSONRenderer,)


class Bodypart_list(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    queryset = Bodypart.objects.all()
    serializer_class = BodypartSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('bodypart',)
    search_fields = ('bodypart',)
    renderer_classes = (JSONRenderer,)


class Measurement_list(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('id',)
    renderer_classes = (JSONRenderer,)


class Insurance_list(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    queryset = Insurance.objects.all()
    serializer_class = InsuranceSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('id',)
    search_fields = ('insurance_plan',)
    renderer_classes = (JSONRenderer,)


class Procedure_list(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    queryset = Procedure.objects.all()
    serializer_class = ProcedureSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('bodypart',)
    search_fields = ('procedure_name',)
    renderer_classes = (JSONRenderer,)


class Doctor_Note_list(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    queryset = Doctor_Note.objects.all()
    serializer_class = Doctor_NoteSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    renderer_classes = (JSONRenderer,)


class Medicine_Note_list(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    queryset = Medicine_Note.objects.all()
    serializer_class = Medicine_NoteSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    renderer_classes = (JSONRenderer,)


class Profile_show(APIView):
    def get_object(self, pk):
        try:
            return Profile.objects.get(pk=pk)

        except Profile.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        profile = Profile.objects.get(pk=pk)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

    def post(self, request, pk, format=None):
        profile = self.get_object(pk)
        serializer = ProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        profile = profile.get_object(pk)
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Procedure_Images_list(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    queryset = Procedure_Images.objects.all()
    serializer_class = Procedure_ImagesSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    renderer_classes = (JSONRenderer,)


class Procedure_Videos_list(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    queryset = Procedure_Videos.objects.all()
    serializer_class = Procedure_VideosSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    renderer_classes = (JSONRenderer,)


class Procedure_Helpline_list(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    queryset = Procedure_Helpline.objects.all()
    serializer_class = Procedure_HelplineSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    renderer_classes = (JSONRenderer,)


class Procedure_Note_list(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    queryset = Procedure_Note.objects.all()
    serializer_class = Procedure_NoteSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    renderer_classes = (JSONRenderer,)


class MyDoctorsapi(APIView):
    renderer_classes=(JSONRenderer,)
    # def get_object(self, pk):
    #     try:
    #         return Doctor.objects.get(pk=pk)
    
    #     except Doctor.DoesNotExist:
    #         raise Http404

    def get(self, request, id1, format=None):
        doctor = Doctor.objects.filter(user__id=id1)
        serializer = DoctorSerializer(doctor, many = True)
        return Response(serializer.data)

    # def post(self, request, pk, format=None):
    #     doctor = self.get_object(pk)
    #     serializer = DoctorSerializer(doctor, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    # def delete(self, request, pk):
    #     doctor = Doctor.get_object(pk)
    #     doctor.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)

class MyDoctorNotesapi(APIView):
#     permission_classes=(IsAuthenticated,)
    renderer_classes=(JSONRenderer,)
#     def get_object(self, pk):
#         try:
#             return Disease.objects.get(pk=pk)

#         except Disease.DoesNotExist:
#             raise Http404

    def get(self, request, id1,id2, format=None):
        doctor_note =Doctor_Note.objects.filter(user__id=id1).filter(doctor__id=id2)
        serializer = Doctor_NoteSerializer(doctor_note,many = True)
        return Response(serializer.data)

class MyMedicineapi(APIView):
    # def get_object(self, pk):
    #     try:
    #         return Medicine.objects.get(pk=pk)

    #     except Medicine.DoesNotExist:
    #         raise Http404

    def get(self, request, id1, format=None):
        medicine = Medicine.objects.filter(user__id=id1)
        serializer = MedicineSerializer(medicine,many=True)
        return Response(serializer.data)

    # def post(self, request, pk, format=None):
    #     doctor = self.get_object(pk)
    #     serializer = MedicineSerializer(medicine, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    # def delete(self, request, pk):
    #     medicine = Medicine.get_object(pk)
    #     medicine.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)


class MyMedicineNotesapi(APIView):
#     permission_classes=(IsAuthenticated,)
    renderer_classes=(JSONRenderer,)
#     def get_object(self, pk):
#         try:
#             return Disease.objects.get(pk=pk)

#         except Disease.DoesNotExist:
#             raise Http404

    def get(self, request, id1,id2, format=None):
        medicine_note =Medicine_Note.objects.filter(user__id=id1).filter(medicine__id=id2)
        serializer = Medicine_NoteSerializer(medicine_note,many = True)
        return Response(serializer.data)

class MyDiseasesapi(APIView):
    permission_classes=(IsAuthenticated,)
    renderer_classes=(JSONRenderer,)
#     def get_object(self, pk):
#         try:
#             return Disease.objects.get(pk=pk)

#         except Disease.DoesNotExist:
#             raise Http404

    def get(self, request, id1, format=None):
        disease = Disease.objects.filter(user__id=id1)
        serializer = DiseaseSerializer(disease,many = True)
        return Response(serializer.data)

class MyDiseaseNotesapi(APIView):
    #permission_classes=(IsAuthenticated,)
    renderer_classes=(JSONRenderer,)
#     def get_object(self, pk):
#         try:
#             return Disease.objects.get(pk=pk)

#         except Disease.DoesNotExist:
#             raise Http404

    def get(self, request, id1,id2, format=None):
        disease_note =Disease_Note.objects.filter(user__id=id1).filter(disease__id=id2)
        serializer = Disease_NoteSerializer(disease_note,many = True)
        return Response(serializer.data)


class MyAppointmentsapi(APIView):
#     permission_classes=(IsAuthenticated,)
    renderer_classes=(JSONRenderer,)
#     def get_object(self, pk):
#         try:
#             return Disease.objects.get(pk=pk)

#         except Disease.DoesNotExist:
#             raise Http404

    def get(self, request, id1, format=None):
        appointment =Appointment.objects.filter(user__id=id1)
        serializer = AppointmentSerializer(appointment,many = True)
        return Response(serializer.data)


class MyMeasurementsapi(APIView):
#     permission_classes=(IsAuthenticated,)
    renderer_classes=(JSONRenderer,)
#     def get_object(self, pk):
#         try:
#             return Disease.objects.get(pk=pk)

#         except Disease.DoesNotExist:
#             raise Http404

    def get(self, request, id1, format=None):
        measurement =Measurement.objects.filter(user__id=id1)
        serializer = MeasurementSerializer(measurement,many = True)
        return Response(serializer.data)
    # def post(self, request, pk, format=None):
    #     disease = self.get_object(pk)
    #     serializer = DiseaseSerializer(disease, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    # def delete(self, request, pk):
    #     disease = Disease.get_object(pk)
    #     disease.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)

class MyInsurancesapi(APIView):
#     permission_classes=(IsAuthenticated,)
    renderer_classes=(JSONRenderer,)
#     def get_object(self, pk):
#         try:
#             return Disease.objects.get(pk=pk)

#         except Disease.DoesNotExist:
#             raise Http404

    def get(self, request, id1, format=None):
        insurance =Insurance.objects.filter(user__id=id1)
        serializer = InsuranceSerializer(insurance,many = True)
        return Response(serializer.data)


# class MyProceduresapi(APIView):
#     permission_classes=(IsAuthenticated,)
#     renderer_classes=(JSONRenderer,)
#     # def get_object(self, pk):
#     #     try:
#     #         return Procedure.objects.get(pk=pk)

#     #     except Procedure.DoesNotExist:
#     #         raise Http404

#     def get(self, request, id1, format=None):
#         procedure = Procedure.objects.filter(user__id=id1)
#         serializer = ProcedureSerializer(procedure,many=True)
#         return Response(serializer.data)

    # def post(self, request, pk, format=None):
    #     procedure = self.get_object(pk)
    #     serializer = ProcedureSerializer(Procedure, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    # def delete(self, request, pk):
    #     procedure = Procedure.get_object(pk)
    #     procedure.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)




# class Symptom_show(APIView):
#     def get_object(self, pk):
#         try:
#             return Symptom.objects.get(pk=pk)

#         except Symptom.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         symptom = Symptom.objects.get(pk=pk)
#         serializer = SymptomSerializer(bodypart)
#         return Response(serializer.data)

#     def post(self, request, pk, format=None):
#         symptom = self.get_object(pk)
#         serializer = SymptomSerializer(Symptom, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         symptom = Symptom.get_object(pk)
#         symptom.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


class HomeView(generic.TemplateView):
    template_name = 'MyHealthApp/home.html'


def RedirectHomeView(request):
    return HttpResponseRedirect('/home/')


class MyHealthView(generic.TemplateView):
    template_name = 'MyHealthApp/MyHealthApp.html'


# class baseView(generic.TemplateView):
#   template_name = 'HealthApp/MyHealthBase.html'

class sidebarView(generic.TemplateView):
    template_name = 'MyHealthApp/sidebar.html'


@login_required
def MyInsurances(request):
    current_user = request.user
    queryset = Insurance.objects.filter(user_id=current_user.id)
    return render(request, 'MyHealthApp/my-insurance.html', {'insurance_list': queryset})


@login_required
def MyMeasurements(request):
    current_user = request.user
    queryset = Measurement.objects.filter(user_id=current_user.id)
    return render(request, 'MyHealthApp/my-measurements.html', {'measurement_list': queryset})


@login_required
def MyDiseases(request):
    current_user = request.user
    queryset = current_user.disease_set.all()
    return render(request, 'MyHealthApp/my-diseases.html', {'disease_list': queryset})


@login_required
def MyDocuments(request):
    current_user = request.user
    queryset = Document.objects.filter(user_id=current_user.id)
    return render(request, 'MyHealthApp/my-documents.html', {'document_list': queryset})


@login_required
def MyDoctors(request):
    current_user = request.user
    queryset = current_user.doctor_set.all()
    return render(request, 'MyHealthApp/my-doctors.html', {'doctor_list': queryset})


@login_required
def MyAppointments(request):
    current_user = request.user
    queryset = Appointment.objects.filter(user_id=current_user.id)
    return render(request, 'MyHealthApp/my-appointments.html', {'appointment_list': queryset})


@login_required
def MyMedicines(request):
    current_user = request.user
    queryset = current_user.medicine_set.all()

    if not request.user.is_authenticated:
        context = "Please log in first."
        return render(request, 'GeneralApp/login.html', {'form': form, 'context': context})
        # return redirect('/')
    if request.user.get_username() == '':
        context = "Please log in first."
        return render(request, 'GeneralApp/login.html', {'context': context})
        # Context is not showing up, see if need to import views/urls in ProfileApp
    # return render(request, 'dashboard.html', {'current_user': current_user})
    return render(request, 'MyHealthApp/my-medicines.html', {'medicine_list': queryset})


@login_required
def AddDocument(request):
    
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            temp_instance = form.save(commit=False)
            temp_instance.user = request.user
            temp_instance.save()
            return HttpResponseRedirect('/my_documents')
        else:
            print form.errors
    else:
        form = DocumentForm()
    return render(request, 'MyHealthApp/add_document.html', {'form': form})


@login_required
def AddInsurance(request):
    if request.method == 'POST':
        form = InsuranceForm(request.POST, request.FILES)
        if form.is_valid():
            temp_instance = form.save(commit=False)
            temp_instance.user = request.user
            temp_instance.save()
            return HttpResponseRedirect('/my_insurances')
        else:
            print form.errors
    else:
        form = InsuranceForm()
    return render(request, 'MyHealthApp/add_insurance.html', {'form': form})


@login_required
def AddMeasurement(request):
    if request.method == 'POST':
        form = MeasurementForm(request.POST, request.FILES)
        if form.is_valid():
            temp_instance = form.save(commit=False)
            temp_instance.user = request.user
            temp_instance.save()
            return HttpResponseRedirect('/my_measurements')
        else:
            print form.errors
    else:
        form = MeasurementForm()
    return render(request, 'MyHealthApp/add_measurement.html', {'form': form})


@login_required
def AddDoctor(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST, request.FILES)
        if form.is_valid():
            temp_instance = form.save(commit=False)
            temp_instance.save()
            temp_instance.user.add(request.user)
            temp_instance.save()
            return HttpResponseRedirect('/my_doctors')
        else:
            print form.errors
    else:
        form = DoctorForm()
    return render(request, 'MyHealthApp/add_doctor.html', {'form': form})


@login_required
def AddAppointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST, user=request.user)
        if form.is_valid():
            temp_instance = form.save(commit=False)
            temp_instance.user = request.user
            temp_instance.save()
            return HttpResponseRedirect('/my_appointments')
        else:
            print form.errors
    else:
        form = AppointmentForm(user=request.user)
    return render(request, 'MyHealthApp/add_appointment.html', {'form': form})


@login_required
def AddMedicine(request):
    if request.method == 'POST':
        form = MedicineForm(request.POST, user=request.user)
        if form.is_valid():
            temp_instance = form.save(commit=False)
            temp_instance.save()
            temp_instance.user.add(request.user)
            temp_instance.save()
            return HttpResponseRedirect('/my_medicines')
        else:
            print form.errors
    else:
        form = MedicineForm(user=request.user)
    return render(request, 'MyHealthApp/add_medicine.html', {'form': form})


@login_required
def AddDisease(request):
    if request.method == 'POST':
        form = DiseaseForm(request.POST, user=request.user)
        if form.is_valid():
            temp_instance = form.save(commit=False)
            temp_instance.save()
            temp_instance.user.add(request.user)
            temp_instance.save()
            return HttpResponseRedirect('/my_diseases')
        else:
            print form.errors
    else:
        form = DiseaseForm(user=request.user)
    return render(request, 'MyHealthApp/add_disease.html', {'form': form})


@login_required
def EditDocument(request, docu_id):
    current_user = request.user
    queryset = Document.objects.filter(user_id=current_user.id)
    document = Document.objects.get(id=docu_id)

    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES, instance=document)
        if form.is_valid():
            temp_instance = form.save(commit=False)
            temp_instance.user = request.user
            temp_instance.save()
            return HttpResponseRedirect('/my_documents')
        else:
            print form.errors
    else:
        form = DocumentForm(instance=document)
    return render(request, 'MyHealthApp/edit_document.html',
                  {'form': form, 'document_list': queryset, 'current_document': document})


@login_required
def EditInsurance(request, ins_id):
    current_user = request.user
    queryset = Insurance.objects.filter(user_id=current_user.id)
    insurance = Insurance.objects.get(id=ins_id)

    if request.method == 'POST':
        form = InsuranceForm(request.POST, request.FILES, instance=insurance)
        if form.is_valid():
            temp_instance = form.save(commit=False)
            temp_instance.user = request.user
            temp_instance.save()
            return HttpResponseRedirect('/my_insurances')
        else:
            print form.errors
    else:
        form = InsuranceForm(instance=insurance)
    return render(request, 'MyHealthApp/edit_insurance.html',
                  {'form': form, 'insurance_list': queryset, 'current_insurance': insurance})


@login_required
def EditMeasurement(request, mes_id):
    current_user = request.user
    queryset = Measurement.objects.filter(user_id=current_user.id)
    measurement = Measurement.objects.get(id=mes_id)

    if request.method == 'POST':
        form = MeasurementForm(request.POST, request.FILES, instance=measurement)
        if form.is_valid():
            temp_instance = form.save(commit=False)
            temp_instance.user = request.user
            temp_instance.save()
            return HttpResponseRedirect('/my_measurements')
        else:
            print form.errors
    else:
        form = MeasurementForm(instance=measurement)
    return render(request, 'MyHealthApp/edit_measurement.html',
                  {'form': form, 'measurement_list': queryset, 'current_measurement': measurement})


@login_required
def EditAppointment(request, app_id):
    current_user = request.user
    queryset = Appointment.objects.filter(user_id=request.user.id)
    appointment = Appointment.objects.get(id=app_id)

    if request.method == 'POST':
        form = AppointmentForm(request.POST, user=request.user, instance=appointment)
        if form.is_valid():
            temp_instance = form.save(commit=False)
            temp_instance.user = request.user
            temp_instance.save()
            return HttpResponseRedirect('/my_appointments')
        else:
            print form.errors
    else:
        form = AppointmentForm(user=request.user, instance=appointment)
    return render(request, 'MyHealthApp/edit_appointment.html',
                  {'form': form, 'appointment_list':queryset,'current_appointment': appointment})


@login_required
def EditDoctor(request, doc_id):
    current_user = request.user
    queryset = current_user.doctor_set.all()
    doctor = Doctor.objects.get(id=doc_id)

    if request.method == 'POST':
        form = DoctorForm(request.POST, request.FILES, instance=doctor)
        if form.is_valid():
            temp_instance = form.save(commit=False)
            temp_instance.save()
            temp_instance.user.add(request.user)
            temp_instance.save()
            return HttpResponseRedirect('/my_doctors')
        else:
            print form.errors
    else:
        form = DoctorForm(instance=doctor)
    return render(request, 'MyHealthApp/edit_doctor.html',
                  {'form': form, 'doctor_list': queryset, 'current_doctor': doctor})


@login_required
def EditDisease(request, dis_id):
    current_user = request.user
    queryset = current_user.disease_set.all()
    disease = Disease.objects.get(id=dis_id)

    if request.method == 'POST':
        form = DiseaseForm(request.POST, user=request.user, instance=disease)
        if form.is_valid():
            temp_instance = form.save(commit=False)
            temp_instance.save()
            temp_instance.user.add(request.user)
            temp_instance.save()
            return HttpResponseRedirect('/my_diseases')
        else:
            print form.errors
    else:
        form = DiseaseForm(user=request.user, instance=disease)
    return render(request, 'MyHealthApp/edit_disease.html',
                  {'form': form, 'disease_list': queryset, 'current_disease': disease})


@login_required
def EditMedicine(request, med_id):
    current_user = request.user
    medicine = Medicine.objects.get(id=med_id)
    queryset = current_user.medicine_set.all()

    if request.method == 'POST':
        form = MedicineForm(request.POST, user=request.user, instance=medicine)
        if form.is_valid():
            temp_instance = form.save(commit=False)
            temp_instance.save()
            temp_instance.user.add(request.user)
            temp_instance.save()
            return HttpResponseRedirect('/my_medicines')
        else:
            print form.errors
    else:
        form = MedicineForm(user=request.user, instance=medicine)
    return render(request, 'MyHealthApp/edit_medicine.html',
                  {'form': form, 'medicine_list': queryset, 'current_medicine': medicine})


@login_required
def DeleteInsurance(request, ins_id):
    get_object_or_404(Insurance, pk=ins_id).delete()
    return HttpResponseRedirect('/my_insurances')


@login_required
def DeleteDocument(request, docu_id):
    get_object_or_404(Document, pk=docu_id).delete()
    return HttpResponseRedirect('/my_documents')


@login_required
def DeleteAppointment(request, app_id):
    get_object_or_404(Appointment, pk=app_id).delete()
    return HttpResponseRedirect('/my_appointments')


@login_required
def DeleteMeasurement(request, mes_id):
    get_object_or_404(Measurement, pk=mes_id).delete()
    return HttpResponseRedirect('/my_measurements')


@login_required
def DeleteMedicine(request, med_id):
    current_user = request.user
    current_user.medicine_set.remove(Medicine.objects.get(pk=med_id))
    return HttpResponseRedirect('/my_medicines')


@login_required
def DeleteDisease(request, dis_id):
    current_user = request.user
    current_user.disease_set.remove(Disease.objects.get(pk=dis_id))
    return HttpResponseRedirect('/my_diseases')


@login_required
def DeleteDoctor(request, doc_id):
    current_user = request.user
    current_user.doctor_set.remove(Doctor.objects.get(pk=doc_id))
    return HttpResponseRedirect('/my_doctors')

