
# Create your models here.

from django.db import models

class Patient(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	date_of_birth = models.DateField()
	email = models.EmailField(unique=True)
	phone = models.CharField(max_length=20, blank=True)

	def __str__(self):
		return f"{self.first_name} {self.last_name}"

class Doctor(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	specialty = models.CharField(max_length=100, blank=True)
	email = models.EmailField(unique=True)
	phone = models.CharField(max_length=20, blank=True)

	def __str__(self):
		return f"Dr. {self.first_name} {self.last_name}"

class HealthRecord(models.Model):
	patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='health_records')
	doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, related_name='health_records')
	record_date = models.DateField()
	diagnosis = models.TextField()
	treatment = models.TextField(blank=True)

	def __str__(self):
		return f"Record for {self.patient} on {self.record_date}"
