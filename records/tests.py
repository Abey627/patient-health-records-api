
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Patient, Doctor, Appointment, Prescription, HealthRecord

class PatientAPITestCase(APITestCase):
	def setUp(self):
		self.patient_data = {
			'first_name': 'John',
			'last_name': 'Doe',
			'date_of_birth': '1990-01-01',
			'email': 'john@example.com',
			'phone': '1234567890'
		}
		self.patient = Patient.objects.create(**self.patient_data)

	def test_create_patient(self):
		url = reverse('patient-list-create')
		data = {
			'first_name': 'Jane',
			'last_name': 'Smith',
			'date_of_birth': '1985-05-05',
			'email': 'jane@example.com',
			'phone': '0987654321'
		}
		response = self.client.post(url, data)
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

	def test_get_patient(self):
		url = reverse('patient-detail', args=[self.patient.id])
		response = self.client.get(url)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response.data['email'], self.patient.email)

	def test_update_patient(self):
		url = reverse('patient-detail', args=[self.patient.id])
		data = {'phone': '1112223333'}
		response = self.client.patch(url, data)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.patient.refresh_from_db()
		self.assertEqual(self.patient.phone, '1112223333')

	def test_delete_patient(self):
		url = reverse('patient-detail', args=[self.patient.id])
		response = self.client.delete(url)
		self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class DoctorAPITestCase(APITestCase):
	def setUp(self):
		self.doctor_data = {
			'first_name': 'Alice',
			'last_name': 'Brown',
			'specialty': 'Cardiology',
			'email': 'alice@example.com',
			'phone': '5551234567'
		}
		self.doctor = Doctor.objects.create(**self.doctor_data)

	def test_create_doctor(self):
		url = reverse('doctor-list-create')
		data = {
			'first_name': 'Bob',
			'last_name': 'White',
			'specialty': 'Neurology',
			'email': 'bob@example.com',
			'phone': '5559876543'
		}
		response = self.client.post(url, data)
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

	def test_get_doctor(self):
		url = reverse('doctor-detail', args=[self.doctor.id])
		response = self.client.get(url)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response.data['email'], self.doctor.email)

	def test_update_doctor(self):
		url = reverse('doctor-detail', args=[self.doctor.id])
		data = {'phone': '5550001111'}
		response = self.client.patch(url, data)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.doctor.refresh_from_db()
		self.assertEqual(self.doctor.phone, '5550001111')

	def test_delete_doctor(self):
		url = reverse('doctor-detail', args=[self.doctor.id])
		response = self.client.delete(url)
		self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class AppointmentAPITestCase(APITestCase):
	def setUp(self):
		self.patient = Patient.objects.create(
			first_name='Ann', last_name='Lee', date_of_birth='1980-02-02', email='ann@example.com', phone='2223334444')
		self.doctor = Doctor.objects.create(
			first_name='Greg', last_name='House', specialty='General', email='greg@example.com', phone='3334445555')
		self.appointment_data = {
			'patient_id': self.patient.id,
			'doctor_id': self.doctor.id,
			'appointment_datetime': '2025-10-01T10:00:00Z',
			'status': 'scheduled'
		}
		self.appointment = Appointment.objects.create(
			patient=self.patient, doctor=self.doctor, appointment_datetime='2025-10-01T10:00:00Z', status='scheduled')

	def test_create_appointment(self):
		url = reverse('appointment-list-create')
		data = {
			'patient_id': self.patient.id,
			'doctor_id': self.doctor.id,
			'appointment_datetime': '2025-10-02T11:00:00Z',
			'status': 'scheduled'
		}
		response = self.client.post(url, data)
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

	def test_get_appointment(self):
		url = reverse('appointment-detail', args=[self.appointment.id])
		response = self.client.get(url)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response.data['status'], self.appointment.status)

	def test_update_appointment(self):
		url = reverse('appointment-detail', args=[self.appointment.id])
		data = {'status': 'completed'}
		response = self.client.patch(url, data)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.appointment.refresh_from_db()
		self.assertEqual(self.appointment.status, 'completed')

	def test_delete_appointment(self):
		url = reverse('appointment-detail', args=[self.appointment.id])
		response = self.client.delete(url)
		self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class PrescriptionAPITestCase(APITestCase):
	def setUp(self):
		self.patient = Patient.objects.create(
			first_name='Sam', last_name='Green', date_of_birth='1975-03-03', email='sam@example.com', phone='4445556666')
		self.doctor = Doctor.objects.create(
			first_name='Eve', last_name='Black', specialty='Pediatrics', email='eve@example.com', phone='5556667777')
		self.appointment = Appointment.objects.create(
			patient=self.patient, doctor=self.doctor, appointment_datetime='2025-10-03T12:00:00Z', status='scheduled')
		self.prescription_data = {
			'appointment_id': self.appointment.id,
			'medication': 'Ibuprofen',
			'dosage': '200mg',
			'instructions': 'Take after meals'
		}
		self.prescription = Prescription.objects.create(
			appointment=self.appointment, medication='Ibuprofen', dosage='200mg', instructions='Take after meals')

	def test_create_prescription(self):
		url = reverse('prescription-list-create')
		data = {
			'appointment_id': self.appointment.id,
			'medication': 'Paracetamol',
			'dosage': '500mg',
			'instructions': 'Twice daily'
		}
		response = self.client.post(url, data)
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

	def test_get_prescription(self):
		url = reverse('prescription-detail', args=[self.prescription.id])
		response = self.client.get(url)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response.data['medication'], self.prescription.medication)

	def test_update_prescription(self):
		url = reverse('prescription-detail', args=[self.prescription.id])
		data = {'dosage': '400mg'}
		response = self.client.patch(url, data)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.prescription.refresh_from_db()
		self.assertEqual(self.prescription.dosage, '400mg')

	def test_delete_prescription(self):
		url = reverse('prescription-detail', args=[self.prescription.id])
		response = self.client.delete(url)
		self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class HealthRecordAPITestCase(APITestCase):
	def setUp(self):
		self.patient = Patient.objects.create(
			first_name='Tom', last_name='Blue', date_of_birth='1965-04-04', email='tom@example.com', phone='7778889999')
		self.doctor = Doctor.objects.create(
			first_name='Sue', last_name='Yellow', specialty='Dermatology', email='sue@example.com', phone='8889990000')
		self.healthrecord_data = {
			'patient_id': self.patient.id,
			'doctor_id': self.doctor.id,
			'record_date': '2025-09-01',
			'diagnosis': 'Flu',
			'treatment': 'Rest and fluids'
		}
		self.healthrecord = HealthRecord.objects.create(
			patient=self.patient, doctor=self.doctor, record_date='2025-09-01', diagnosis='Flu', treatment='Rest and fluids')

	def test_create_healthrecord(self):
		url = reverse('healthrecord-list-create')
		data = {
			'patient_id': self.patient.id,
			'doctor_id': self.doctor.id,
			'record_date': '2025-09-02',
			'diagnosis': 'Cold',
			'treatment': 'Medication'
		}
		response = self.client.post(url, data)
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

	def test_get_healthrecord(self):
		url = reverse('healthrecord-detail', args=[self.healthrecord.id])
		response = self.client.get(url)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response.data['diagnosis'], self.healthrecord.diagnosis)

	def test_update_healthrecord(self):
		url = reverse('healthrecord-detail', args=[self.healthrecord.id])
		data = {'treatment': 'Antibiotics'}
		response = self.client.patch(url, data)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.healthrecord.refresh_from_db()
		self.assertEqual(self.healthrecord.treatment, 'Antibiotics')

	def test_delete_healthrecord(self):
		url = reverse('healthrecord-detail', args=[self.healthrecord.id])
		response = self.client.delete(url)
		self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
