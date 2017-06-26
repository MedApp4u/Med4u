from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Measurement, Doctor, Doctor_Note, Medicine_Note, Medicine, Bodypart, Appointment, Symptom, \
    Insurance, Procedure
# from .serializers import DoctorSerializer,Doctor_NoteSerializer,Medicine_NoteSerializer,MedicineSerializer,MeasurementSerializer, BodypartSerializer, SymptomSerializer , InsuranceSerializer, ProcedureSerializer, AppointmentSerializer
from .serializers import *
from rest_framework.views import APIView
from ProfileApp.models import Profile
from ProfileApp.serializers import ProfileSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework import generics
from django.views import generic


# Create your views here

class Doctor_list(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('doctor_speciality',)
    search_fields = ('doctor_name',)


'''
@api_view(['GET','POST'])
def Medicine_list(request):
    if request.method == 'GET':
        medicines = Medicine.objects.all()
        serializer = MedicineSerializer(medicines,many=True)
        return Response(serializer.data)

    elif request.method =='POST':
        serializer = MedicineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data)
        return Response(serializer.errors)
'''


class Medicine_list(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('method',)
    search_fields = ('medicine_name',)


class Appointment_list(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('date',)


class Symptom_list(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    queryset = Symptom.objects.all()
    serializer_class = SymptomSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)


class Bodypart_list(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    queryset = Bodypart.objects.all()
    serializer_class = BodypartSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('bodypart',)
    search_fields = ('bodypart',)


class Measurement_list(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('weight',)


class Insurance_list(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    queryset = Insurance.objects.all()
    serializer_class = InsuranceSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('expiry_date',)
    search_fields = ('insurance_plan',)


class Procedure_list(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    queryset = Procedure.objects.all()
    serializer_class = ProcedureSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('bodypart',)
    search_fields = ('procedure_name',)


class Doctor_Note_list(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    queryset = Doctor_Note.objects.all()
    serializer_class = Doctor_NoteSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)


class Medicine_Note_list(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    queryset = Medicine_Note.objects.all()
    serializer_class = Medicine_NoteSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)


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


class Procedure_Videos_list(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    queryset = Procedure_Videos.objects.all()
    serializer_class = Procedure_VideosSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)


class Procedure_Helpline_list(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    queryset = Procedure_Helpline.objects.all()
    serializer_class = Procedure_HelplineSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)


class Procedure_Note_list(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    queryset = Procedure_Note.objects.all()
    serializer_class = Procedure_NoteSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)


def ViewInsurance(request):
    current_user = request.user
    # all_insurances = current_user.insurance_set.all()
    return render(request, 'view_insurance.html', {'all_insurances': current_user.insurance_set.all().first()})


class Doctor_show(APIView):
    def get_object(self, pk):
        try:
            return Doctor.objects.get(pk=pk)

        except Doctor.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        doctor = Doctor.objects.get(pk=pk)
        serializer = DoctorSerializer(doctor)
        return Response(serializer.data)

    def post(self, request, pk, format=None):
        doctor = self.get_object(pk)
        serializer = DoctorSerializer(doctor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        doctor = Doctor.get_object(pk)
        doctor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Medicine_show(APIView):
    def get_object(self, pk):
        try:
            return Medicine.objects.get(pk=pk)

        except Medicine.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        medicine = Medicine.objects.get(pk=pk)
        serializer = MedicineSerializer(medicine)
        return Response(serializer.data)

    def post(self, request, pk, format=None):
        doctor = self.get_object(pk)
        serializer = MedicineSerializer(medicine, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        medicine = Medicine.get_object(pk)
        medicine.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Disease_show(APIView):
    def get_object(self, pk):
        try:
            return Disease.objects.get(pk=pk)

        except Disease.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        disease = Disease.objects.get(pk=pk)
        serializer = DiseaseSerializer(disease)
        return Response(serializer.data)

    def post(self, request, pk, format=None):
        disease = self.get_object(pk)
        serializer = DiseaseSerializer(disease, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        disease = Disease.get_object(pk)
        disease.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Procedure_show(APIView):
    def get_object(self, pk):
        try:
            return Procedure.objects.get(pk=pk)

        except Procedure.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        procedure = Procedure.objects.get(pk=pk)
        serializer = ProcedureSerializer(procedure)
        return Response(serializer.data)

    def post(self, request, pk, format=None):
        procedure = self.get_object(pk)
        serializer = ProcedureSerializer(Procedure, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        procedure = Procedure.get_object(pk)
        procedure.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Bodypart_show(APIView):
    def get_object(self, pk):
        try:
            return Bodypart.objects.get(pk=pk)

        except Bodypart.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        bodypart = Bodypart.objects.get(pk=pk)
        serializer = BodypartSerializer(bodypart)
        return Response(serializer.data)

    def post(self, request, pk, format=None):
        bodypart = self.get_object(pk)
        serializer = BodypartSerializer(Bodypart, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        bodypart = Bodypart.get_object(pk)
        bodypart.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Symptom_show(APIView):
    def get_object(self, pk):
        try:
            return Symptom.objects.get(pk=pk)

        except Symptom.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        symptom = Symptom.objects.get(pk=pk)
        serializer = SymptomSerializer(bodypart)
        return Response(serializer.data)

    def post(self, request, pk, format=None):
        symptom = self.get_object(pk)
        serializer = SymptomSerializer(Symptom, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        symptom = Symptom.get_object(pk)
        symptom.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# def get(self, request, *args, **kwargs):
# return self.retrieve(request, *args, **kwargs)

# def put(self, request, *args, **kwargs):
#     return self.update(request, *args, **kwargs)

# def delete(self, request, *args, **kwargs):
#     return self.destroy(request, *args, **kwargs)

class HomeView(generic.TemplateView):
    template_name = 'MyHealthApp/home.html'


class SymptomsView(generic.TemplateView):
    template_name = 'MyHealthApp/symptoms.html'


class MyHealthView(generic.TemplateView):
    template_name = 'MyHealthApp/MyHealthApp.html'


# class baseView(generic.TemplateView):
#   template_name = 'HealthApp/MyHealthBase.html'

class sidebarView(generic.TemplateView):
    template_name = 'MyHealthApp/sidebar.html'


def ViewInsurance(request):
    current_user = request.user
    queryset = Insurance.objects.filter(user_id=current_user.id)
    return render(request, 'MyHealthApp/my-insurance.html', {'insurance_list': queryset})


def ViewMeasurement(request):
    current_user = request.user
    queryset = Measurement.objects.filter(user_id=current_user.id)
    return render(request, 'MyHealthApp/my-measurements.html', {'measurement_list': queryset})