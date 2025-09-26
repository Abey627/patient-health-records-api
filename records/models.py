

from django.db import models
from django.contrib.auth.models import User


# UserProfile: Extends Django User with a role field (Doctor/Patient).
class UserProfile(models.Model):
	ROLE_CHOICES = [
		('doctor', 'Doctor'),
		('patient', 'Patient'),
	]
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
	role = models.CharField(max_length=10, choices=ROLE_CHOICES)

	def __str__(self):
		return f"{self.user.username} ({self.role})"

# Patient: Stores demographic and contact information for individuals receiving medical care.
class Patient(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	date_of_birth = models.DateField()
	email = models.EmailField(unique=True)
	phone = models.CharField(max_length=20, blank=True)

	def __str__(self):
		return f"{self.first_name} {self.last_name}"

# Doctor: Represents medical professionals, including their specialization and contact details.
class Doctor(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	specialty = models.CharField(max_length=100, blank=True)
	email = models.EmailField(unique=True)
	phone = models.CharField(max_length=20, blank=True)

	def __str__(self):
		return f"Dr. {self.first_name} {self.last_name}"

# Appointment: Links a patient and a doctor for a scheduled meeting, tracks date/time and status.
class Appointment(models.Model):
	STATUS_CHOICES = [
		('scheduled', 'Scheduled'),
		('completed', 'Completed'),
		('cancelled', 'Cancelled'),
	]
	patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='appointments')
	doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='appointments')
	appointment_datetime = models.DateTimeField()
	status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='scheduled')

	def __str__(self):
		return f"Appointment: {self.patient} with {self.doctor} at {self.appointment_datetime}"

# Prescription: Contains medication orders and instructions, linked to a specific appointment.
class Prescription(models.Model):
	appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, related_name='prescriptions')
	medication = models.CharField(max_length=200)
	dosage = models.CharField(max_length=100)
	instructions = models.TextField(blank=True)

	def __str__(self):
		return f"Prescription for {self.appointment.patient} - {self.medication}"

# HealthRecord: Stores clinical notes, diagnosis, and treatment details for a patient, authored by a doctor.
class HealthRecord(models.Model):
	patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='health_records')
	doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, related_name='health_records')
	record_date = models.DateField()
	diagnosis = models.TextField()
	treatment = models.TextField(blank=True)

	def __str__(self):
		return f"Record for {self.patient} on {self.record_date}"
