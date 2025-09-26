# Model and Database Design

This document describes the data models and database relationships for the Patient Health Records API project.

## Models

### Patient
- **first_name**: CharField, max_length=100
- **last_name**: CharField, max_length=100
- **date_of_birth**: DateField
- **email**: EmailField, unique
- **phone**: CharField, max_length=20, optional

### Doctor
- **first_name**: CharField, max_length=100
- **last_name**: CharField, max_length=100
- **specialty**: CharField, max_length=100, optional
- **email**: EmailField, unique
- **phone**: CharField, max_length=20, optional


### HealthRecord
- **patient**: ForeignKey to Patient (CASCADE)
- **doctor**: ForeignKey to Doctor (SET_NULL, nullable)
- **record_date**: DateField
- **diagnosis**: TextField
- **treatment**: TextField, optional

#### Design Note: Doctor Field Deletion Behavior
The `doctor` field in `HealthRecord` uses `on_delete=models.SET_NULL`. This means if a doctor is deleted, the related health records will remain, but their `doctor` field will be set to `NULL`. This preserves historical patient data and avoids accidental loss of health records when a doctor leaves or is removed from the system. If you want health records to be deleted along with the doctor, use `on_delete=models.CASCADE` instead.

## Relationships
- Each `HealthRecord` is linked to one `Patient` and one `Doctor`.
- A `Patient` can have multiple `HealthRecord` entries.
- A `Doctor` can be associated with multiple `HealthRecord` entries.

## Design Rationale
- Using separate models for Patient and Doctor avoids data duplication and supports future features (e.g., doctor management).
- Foreign keys ensure referential integrity and enable efficient queries.
- Optional fields allow flexibility for incomplete data.

Refer to this document for understanding and extending the database schema.
