# Serializers and API Views Design

This document describes the design and structure of serializers and API views for the Patient Health Records API project.

## Serializers
Serializers are defined in `records/serializers.py` using Django REST Framework's `ModelSerializer`:

- **PatientSerializer**: Serializes all fields of the `Patient` model.
- **DoctorSerializer**: Serializes all fields of the `Doctor` model.
- **HealthRecordSerializer**: Serializes all fields of the `HealthRecord` model, including nested representations of `Patient` and `Doctor`. Also provides `patient_id` and `doctor_id` for write operations.

## API Views
API views are implemented in `records/views.py` using DRF generic views:

- **PatientListCreateView**: List and create patients.
- **PatientRetrieveUpdateDestroyView**: Retrieve, update, or delete a patient.
- **DoctorListCreateView**: List and create doctors.
- **DoctorRetrieveUpdateDestroyView**: Retrieve, update, or delete a doctor.
- **HealthRecordListCreateView**: List and create health records.
- **HealthRecordRetrieveUpdateDestroyView**: Retrieve, update, or delete a health record.

### Design Rationale
- Using DRF generics provides clean, maintainable CRUD endpoints.
- Nested serializers in `HealthRecordSerializer` allow for rich data representation.
- Primary key fields (`patient_id`, `doctor_id`) simplify write operations and avoid nested object creation.

Refer to this document for understanding and extending the API layer.
