# Model and Database Design

This document describes the data models and database relationships for the Patient Health Records API project.


## Models

### Patient
Stores demographic and contact information for individuals receiving medical care.
- **first_name**: CharField, max_length=100
- **last_name**: CharField, max_length=100
- **date_of_birth**: DateField
- **email**: EmailField, unique
- **phone**: CharField, max_length=20, optional

### Doctor
Represents medical professionals, including their specialization and contact details.
- **first_name**: CharField, max_length=100
- **last_name**: CharField, max_length=100
- **specialty**: CharField, max_length=100, optional
- **email**: EmailField, unique
- **phone**: CharField, max_length=20, optional

### Appointment
Links a patient and a doctor for a scheduled meeting, tracks date/time and status.
- **patient**: ForeignKey to Patient (CASCADE)
- **doctor**: ForeignKey to Doctor (CASCADE)
- **appointment_datetime**: DateTimeField
- **status**: CharField, choices=[scheduled, completed, cancelled], default=scheduled

### Prescription
Contains medication orders and instructions, linked to a specific appointment.
- **appointment**: ForeignKey to Appointment (CASCADE)
- **medication**: CharField, max_length=200
- **dosage**: CharField, max_length=100
- **instructions**: TextField, optional

### HealthRecord
Stores clinical notes, diagnosis, and treatment details for a patient, authored by a doctor.
- **patient**: ForeignKey to Patient (CASCADE)
- **doctor**: ForeignKey to Doctor (SET_NULL, nullable)
- **record_date**: DateField
- **diagnosis**: TextField
- **treatment**: TextField, optional

#### Design Note: Doctor Field Deletion Behavior
The `doctor` field in `HealthRecord` uses `on_delete=models.SET_NULL`. This means if a doctor is deleted, the related health records will remain, but their `doctor` field will be set to `NULL`. This preserves historical patient data and avoids accidental loss of health records when a doctor leaves or is removed from the system. If you want health records to be deleted along with the doctor, use `on_delete=models.CASCADE` instead.


## Relationships
- Each `Appointment` links one `Patient` and one `Doctor`.
- A `Patient` can have multiple `Appointments` and `HealthRecords`.
- A `Doctor` can have multiple `Appointments` and `HealthRecords`.
- Each `Prescription` is linked to one `Appointment` (and thus indirectly to one Patient and one Doctor).
- Each `HealthRecord` is linked to one `Patient` and one `Doctor`.


## Design Rationale
- Using separate models for Patient and Doctor avoids data duplication and supports future features (e.g., doctor management).
- Appointment and Prescription models reflect real-world healthcare workflows and enable tracking of visits and medication orders.
- Foreign keys ensure referential integrity and enable efficient queries.
- Optional fields allow flexibility for incomplete data.

Refer to this document for understanding and extending the database schema.
