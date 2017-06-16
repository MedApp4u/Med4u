from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Measurement,Doctor,Doctor_Note,Medicine_Note, Medicine, Bodypart, Appointment, Symptom, Insurance,Procedure   
from .serializers import DoctorSerializer,Doctor_NoteSerializer,Medicine_NoteSerializer,MedicineSerializer,MeasurementSerializer, BodypartSerializer, SymptomSerializer , InsuranceSerializer, ProcedureSerializer, AppointmentSerializer
from rest_framework.views import APIView
from ProfileApp.models import Profile
from ProfileApp.serializers import ProfileSerializer
from rest_framework.permissions import IsAuthenticated , AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework import generics


#Create your views here
@api_view(['GET','POST'])
def Doctor_list(request):
    if request.method == 'GET':
        doctors = Doctor.objects.all()
        serializer = DoctorSerializer(doctors,many=True)
        return Response(serializer.data)

    elif request.method =='POST':
        serializer = DoctorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
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
    permission_classes(IsAuthenticated,)
    queryset = Medicine.objects.all()
    serializer_class=MedicineSerializer
    filter_backends=(DjangoFilterBackend,SearchFilter)
    filter_fields=('method',)
    search_fields=('medicine_name',)
        
@api_view(['GET','POST'])
def Appointment_list(request):
    if request.method == 'GET':
        appointments = Appointment.objects.all()
        serializer = AppointmentSerializer(appointments,many=True)
        return Response(serializer.data)

    elif request.method =='POST':
        serializer = AppointmentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','POST'])
def Symptom_list(request):
    if request.method == 'GET':
        symptoms = Symptom.objects.all()
        serializer = SymptomSerializer(symptoms,many=True)
        return Response(serializer.data)

    elif request.method =='POST':
        serializer = SymptomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','POST'])
def Bodypart_list(request):
    if request.method == 'GET':
        bodyparts = Bodypart.objects.all()
        serializer = BodypartSerializer(bodyparts,many=True)
        return Response(serializer.data)

    elif request.method =='POST':
        serializer = BodypartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','POST'])
def Measurement_list(request):
    if request.method == 'GET':
        measurements = Measurement.objects.all()
        serializer = MeasurementSerializer(measurements,many=True)
        return Response(serializer.data)

    elif request.method =='POST':
        serializer = MeasurementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','POST'])
def Insurance_list(request):
    if request.method == 'GET':
        insurances= Insurance.objects.all()
        serializer = InsuranceSerializer(insurances,many=True)
        return Response(serializer.data)

    elif request.method =='POST':
        serializer = InsuranceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
@api_view(['GET','POST'])
def Procedure_list(request):
    if request.method == 'GET':
        procedures = Procedure.objects.all()
        serializer = ProcedureSerializer(procedures,many=True)
        return Response(serializer.data)

    elif request.method =='POST':
        serializer = ProcedureSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    
@api_view(['GET','POST'])
def DoctorNote_list(request):
    if request.method == 'GET':
        doctornotes = Doctor_Note.objects.all()
        serializer = Doctor_NoteSerializer(doctornotes,many=True)
        return Response(serializer.data)

    elif request.method =='POST':
        serializer = Doctor_NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET','POST'])
def MedicineNote_list(request):
    if request.method == 'GET':
        medicines = Medicine_Note.objects.all()
        serializer = Medicine_NoteSerializer(medicines,many=True)
        return Response(serializer.data)

    elif request.method =='POST':
        serializer = Medicine_NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class Profile_show(APIView):
    def get_object(self, pk):
        try:
            return Profile.objects.get(pk=pk)

        except Profile.DoesNotExist:
            raise Http404

    def get(self,request,pk,format=None):
        profile = Profile.objects.get(pk=pk)
        serializer=ProfileSerializer(profile)
        return Response (serializer.data)
    def post(self,request,pk,format=None):
        profile = self.get_object(pk)
        serializer =ProfileSerializer(profile,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializers.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        profile=profile.get_object(pk)
        profile.delete()
        return Response (status = status.HTTP_204_NO_CONTENT)

    

# def get(self, request, *args, **kwargs):
# return self.retrieve(request, *args, **kwargs)

# def put(self, request, *args, **kwargs):
#     return self.update(request, *args, **kwargs)

# def delete(self, request, *args, **kwargs):
#     return self.destroy(request, *args, **kwargs)
