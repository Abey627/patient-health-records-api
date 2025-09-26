# API URL Patterns Design

This document explains the design and usage of URL patterns for the Patient Health Records API.

## URL Structure
All API endpoints are prefixed with `/api/` for clarity and separation from other routes.

### Patients
- `GET /api/patients/` — List all patients
- `POST /api/patients/` — Create a new patient
- `GET /api/patients/<id>/` — Retrieve a patient by ID
- `PUT /api/patients/<id>/` — Update a patient by ID
- `PATCH /api/patients/<id>/` — Partially update a patient
- `DELETE /api/patients/<id>/` — Delete a patient

### Doctors
- `GET /api/doctors/` — List all doctors
- `POST /api/doctors/` — Create a new doctor
- `GET /api/doctors/<id>/` — Retrieve a doctor by ID
- `PUT /api/doctors/<id>/` — Update a doctor by ID
- `PATCH /api/doctors/<id>/` — Partially update a doctor
- `DELETE /api/doctors/<id>/` — Delete a doctor

### Health Records
- `GET /api/health-records/` — List all health records
- `POST /api/health-records/` — Create a new health record
- `GET /api/health-records/<id>/` — Retrieve a health record by ID
- `PUT /api/health-records/<id>/` — Update a health record by ID
- `PATCH /api/health-records/<id>/` — Partially update a health record
- `DELETE /api/health-records/<id>/` — Delete a health record

## Design Rationale
- Consistent RESTful patterns make endpoints predictable and easy to use for frontend and tester teams.
- Using DRF generic views ensures standard HTTP methods are supported for each resource.
- The `/api/` prefix helps with routing and API documentation.

Refer to this document for endpoint usage and integration.
