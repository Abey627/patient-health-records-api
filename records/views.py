
# Django REST Framework generic views and schema utilities
from rest_framework import generics
from drf_spectacular.utils import extend_schema

# Import models and serializers for each resource
from .models import Patient, Doctor, Appointment, Prescription, HealthRecord
from .serializers import (
	PatientSerializer, DoctorSerializer, AppointmentSerializer,
	PrescriptionSerializer, HealthRecordSerializer
)
from .permissions import IsDoctor, IsPatient

# -----------------------------------------------------------------------------
# Permission Mixins
# -----------------------------------------------------------------------------
class PatientPermissionMixin:
	"""
	Mixin for views that require the user to have the 'patient' role.
	"""
	permission_classes = [IsPatient]

class DoctorPermissionMixin:
	"""
	Mixin for views that require the user to have the 'doctor' role.
	"""
	permission_classes = [IsDoctor]

# -----------------------------------------------------------------------------
# Patient API Views
# -----------------------------------------------------------------------------
class PatientListCreateView(PatientPermissionMixin, generics.ListCreateAPIView):
	queryset = Patient.objects.all()
	serializer_class = PatientSerializer

	@extend_schema(
		description="List and create patients. Requires JWT authentication and 'patient' role.",
		auth=[{'type': 'http', 'scheme': 'bearer'}],
	)
	def get(self, request, *args, **kwargs):
		return super().get(request, *args, **kwargs)

	@extend_schema(
		description="Create a patient. Requires JWT authentication and 'patient' role.",
		auth=[{'type': 'http', 'scheme': 'bearer'}],
	)
	def post(self, request, *args, **kwargs):
		return super().post(request, *args, **kwargs)

class PatientRetrieveUpdateDestroyView(PatientPermissionMixin, generics.RetrieveUpdateDestroyAPIView):
	queryset = Patient.objects.all()
	serializer_class = PatientSerializer

	@extend_schema(
		description="Retrieve, update, or delete a patient. Requires JWT authentication and 'patient' role.",
		auth=[{'type': 'http', 'scheme': 'bearer'}],
	)
	def get(self, request, *args, **kwargs):
		return super().get(request, *args, **kwargs)

# -----------------------------------------------------------------------------
# Doctor API Views
# -----------------------------------------------------------------------------
class DoctorListCreateView(DoctorPermissionMixin, generics.ListCreateAPIView):
	queryset = Doctor.objects.all()
	serializer_class = DoctorSerializer

	@extend_schema(
		description="List and create doctors. Requires JWT authentication and 'doctor' role.",
		auth=[{'type': 'http', 'scheme': 'bearer'}],
	)
	def get(self, request, *args, **kwargs):
		return super().get(request, *args, **kwargs)

	@extend_schema(
		description="Create a doctor. Requires JWT authentication and 'doctor' role.",
		auth=[{'type': 'http', 'scheme': 'bearer'}],
	)
	def post(self, request, *args, **kwargs):
		return super().post(request, *args, **kwargs)

class DoctorRetrieveUpdateDestroyView(DoctorPermissionMixin, generics.RetrieveUpdateDestroyAPIView):
	queryset = Doctor.objects.all()
	serializer_class = DoctorSerializer

	@extend_schema(
		description="Retrieve, update, or delete a doctor. Requires JWT authentication and 'doctor' role.",
		auth=[{'type': 'http', 'scheme': 'bearer'}],
	)
	def get(self, request, *args, **kwargs):
		return super().get(request, *args, **kwargs)

# -----------------------------------------------------------------------------
# Appointment API Views
# -----------------------------------------------------------------------------
class AppointmentListCreateView(PatientPermissionMixin, generics.ListCreateAPIView):
	queryset = Appointment.objects.all()
	serializer_class = AppointmentSerializer

	@extend_schema(
		description="List and create appointments. Requires JWT authentication and 'patient' role.",
		auth=[{'type': 'http', 'scheme': 'bearer'}],
	)
	def get(self, request, *args, **kwargs):
		return super().get(request, *args, **kwargs)

	@extend_schema(
		description="Create an appointment. Requires JWT authentication and 'patient' role.",
		auth=[{'type': 'http', 'scheme': 'bearer'}],
	)
	def post(self, request, *args, **kwargs):
		return super().post(request, *args, **kwargs)

class AppointmentRetrieveUpdateDestroyView(PatientPermissionMixin, generics.RetrieveUpdateDestroyAPIView):
	queryset = Appointment.objects.all()
	serializer_class = AppointmentSerializer

	@extend_schema(
		description="Retrieve, update, or delete an appointment. Requires JWT authentication and 'patient' role.",
		auth=[{'type': 'http', 'scheme': 'bearer'}],
	)
	def get(self, request, *args, **kwargs):
		return super().get(request, *args, **kwargs)

# -----------------------------------------------------------------------------
# Prescription API Views
# -----------------------------------------------------------------------------
class PrescriptionListCreateView(DoctorPermissionMixin, generics.ListCreateAPIView):
	queryset = Prescription.objects.all()
	serializer_class = PrescriptionSerializer

	@extend_schema(
		description="List and create prescriptions. Requires JWT authentication and 'doctor' role.",
		auth=[{'type': 'http', 'scheme': 'bearer'}],
	)
	def get(self, request, *args, **kwargs):
		return super().get(request, *args, **kwargs)

	@extend_schema(
		description="Create a prescription. Requires JWT authentication and 'doctor' role.",
		auth=[{'type': 'http', 'scheme': 'bearer'}],
	)
	def post(self, request, *args, **kwargs):
		return super().post(request, *args, **kwargs)

class PrescriptionRetrieveUpdateDestroyView(DoctorPermissionMixin, generics.RetrieveUpdateDestroyAPIView):
	queryset = Prescription.objects.all()
	serializer_class = PrescriptionSerializer

	@extend_schema(
		description="Retrieve, update, or delete a prescription. Requires JWT authentication and 'doctor' role.",
		auth=[{'type': 'http', 'scheme': 'bearer'}],
	)
	def get(self, request, *args, **kwargs):
		return super().get(request, *args, **kwargs)

# -----------------------------------------------------------------------------
# HealthRecord API Views
# -----------------------------------------------------------------------------
class HealthRecordListCreateView(generics.ListCreateAPIView):
	queryset = HealthRecord.objects.all()
	serializer_class = HealthRecordSerializer

	@extend_schema(
		description="List and create health records. Requires JWT authentication.",
		auth=[{'type': 'http', 'scheme': 'bearer'}],
	)
	def get(self, request, *args, **kwargs):
		return super().get(request, *args, **kwargs)

	@extend_schema(
		description="Create a health record. Requires JWT authentication.",
		auth=[{'type': 'http', 'scheme': 'bearer'}],
	)
	def post(self, request, *args, **kwargs):
		return super().post(request, *args, **kwargs)

class HealthRecordRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
	queryset = HealthRecord.objects.all()
	serializer_class = HealthRecordSerializer

	@extend_schema(
		description="Retrieve, update, or delete a health record. Requires JWT authentication.",
		auth=[{'type': 'http', 'scheme': 'bearer'}],
	)
	def get(self, request, *args, **kwargs):
		return super().get(request, *args, **kwargs)
