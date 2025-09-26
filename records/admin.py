
# Register your models here.

from django.contrib import admin
from .models import UserProfile, Patient, Doctor, Appointment, Prescription, HealthRecord

admin.site.register(UserProfile)
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Appointment)
admin.site.register(Prescription)
admin.site.register(HealthRecord)
