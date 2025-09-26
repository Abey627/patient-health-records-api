# 🏥 Patient Health Records API (Mini EMR)

A simplified **Electronic Medical Records (EMR)** system built with **Django REST Framework**, **PostgreSQL**, and **Redis**.  
This project demonstrates backend engineering best practices for building secure, scalable, and maintainable APIs in healthcare-like domains.

---

## ✨ Features

- **Authentication & Authorization**
  - JWT-based authentication (Django SimpleJWT).
  - Role-based access (Doctor vs Patient).

- **Core Entities**
  - **Patient** – demographic and contact info.
  - **Doctor** – specialization, license number, contact info.
  - **Appointment** – links doctor ↔ patient, datetime, status.
  - **Prescription** – medication, dosage, linked to appointment.
  - **HealthRecord** – clinical notes, diagnosis, and treatment details for a patient, authored by a doctor.

- **API Endpoints**
  - CRUD for Patients, Doctors, Appointments, Prescriptions.
  - Filtering (e.g., all appointments for a patient).
  - Pagination & search.

- **System Features**
  - PostgreSQL for relational data.
  - Redis for caching frequent queries (e.g., patient profile).
  - API documentation via Swagger/OpenAPI.
  - Unit + integration tests.
  - Dockerized setup with `docker-compose`.
  - CI/CD pipeline (GitHub Actions).

---

## 🛠 Tech Stack

- **Backend**: Django, Django REST Framework  
- **Authentication**: Django SimpleJWT  
- **Database**: PostgreSQL  
- **Cache**: Redis  
- **Containerization**: Docker + Docker Compose  
- **Testing**: Pytest / Django Test Framework  
- **Docs**: drf-spectacular or drf-yasg  
- **CI/CD**: GitHub Actions (lint + tests)

---


## 📂 Project Structure

```
patient-health-records-api/
├── phrapi/                   # Django project settings and root URLs
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py           # Main settings (JWT, DRF, DB, etc.)
│   ├── urls.py               # Root URL config (includes records.urls, JWT, docs)
│   └── wsgi.py
│
├── records/                  # Main app: business logic and API
│   ├── migrations/           # DB migrations
│   ├── __init__.py
│   ├── admin.py              # Admin registration
│   ├── apps.py
│   ├── models.py             # Core models: Patient, Doctor, Appointment, etc.
│   ├── permissions.py        # Custom role-based permissions
│   ├── serializers.py        # DRF serializers for all entities
│   ├── signals.py            # UserProfile auto-creation
│   ├── tests.py              # Pytest/DRF test cases
│   ├── urls.py               # App-level API endpoints
│   ├── views.py              # DRF generic views, permission mixins
│
├── docs/                     # Project documentation
│   ├── api_design.md
│   ├── development_steps.md
│   ├── model_design.md
│   ├── testing_design.md
│   ├── url_patterns.md
│   ├── auth_permissions.md
│
├── pytest.ini                # Pytest config
├── requirements.txt          # Python dependencies
├── manage.py                 # Django management script
├── README.md                 # Project overview
└── db.sqlite3                # SQLite DB (dev only)
```

---


## 🚀 Getting Started

### 1️⃣ Clone the Repo
```bash
git clone https://github.com/Abey627/patient-health-records-api.git
cd patient-health-records-api
```

### 2️⃣ Set Up Python Virtual Environment
It is recommended to use a virtual environment to isolate project dependencies:
```bash
python -m venv venv-phrapi
source venv-phrapi/Scripts/activate  # On Windows
# Or
source venv-phrapi/bin/activate      # On macOS/Linux
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
*(Optional but recommended: `python -m pip install --upgrade pip` before this step).*

### 4️⃣ Create a Django Superuser
To access the Django admin interface, create a superuser account:
```bash
python manage.py createsuperuser
```
Follow the prompts to set username, email, and password.

### 5️⃣ Run Development Server
```bash
python manage.py runserver
```

Access at: [http://localhost:8000/](http://localhost:8000/)

Login to admin at: [http://localhost:8000/admin/](http://localhost:8000/admin/)

### 6️⃣ API Documentation (Swagger UI)
Interactive API docs are available via drf-spectacular:
```bash
http://localhost:8000/api/docs/
```
This provides a live, auto-generated OpenAPI/Swagger interface for all endpoints.

---

## 🧪 Running Tests

```bash
pytest
```

---
