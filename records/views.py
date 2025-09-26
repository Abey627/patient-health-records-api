
# Create your views here.

from rest_framework import generics
from .models import Patient, Doctor, HealthRecord
from .serializers import PatientSerializer, DoctorSerializer, HealthRecordSerializer

# Patient API Views
class PatientListCreateView(generics.ListCreateAPIView):
	queryset = Patient.objects.all()
	serializer_class = PatientSerializer

class PatientRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Patient.objects.all()
	serializer_class = PatientSerializer

# Doctor API Views
class DoctorListCreateView(generics.ListCreateAPIView):
	queryset = Doctor.objects.all()
	serializer_class = DoctorSerializer

class DoctorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Doctor.objects.all()
	serializer_class = DoctorSerializer

# HealthRecord API Views
class HealthRecordListCreateView(generics.ListCreateAPIView):
	queryset = HealthRecord.objects.all()
	serializer_class = HealthRecordSerializer

class HealthRecordRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
	queryset = HealthRecord.objects.all()
	serializer_class = HealthRecordSerializer
