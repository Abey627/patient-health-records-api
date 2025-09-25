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
PHRAPI/
├── phrapi/               # Django project
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── records/              # Main app
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   └── urls.py (to be created)
│
├── manage.py
└── README.md
```

---

## 🚀 Getting Started

### 1️⃣ Clone the Repo
```bash
git clone https://github.com/<your-username>/patient-health-records-api.git
cd patient-health-records-api
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

*(Optional but recommended: `python -m pip install --upgrade pip` before this step).*

### 3️⃣ Run Development Server
```bash
python manage.py runserver
```

Access at: [http://localhost:8000/](http://localhost:8000/)

---

## 🧪 Running Tests

```bash
pytest
```

---

## 📌 Roadmap

### Phase 1: Core EMR
- [x] Django + DRF setup
- [x] Project scaffold with `phrapi` + `records` app
- [ ] Models (Patient, Doctor, Appointment, Prescription)
- [ ] CRUD APIs
- [ ] JWT Authentication
- [ ] Swagger/OpenAPI docs

### Phase 2: Enhancements
- [ ] Redis caching (patient profiles)
- [ ] Role-based permissions
- [ ] Unit + integration tests
- [ ] GitHub Actions (CI/CD)
- [ ] Pre-commit hooks (flake8, black, isort)

### Phase 3: Advanced
- [ ] Search + filtering
- [ ] Appointment conflict validation
- [ ] Notification service (email/SMS mock)
- [ ] Metrics & monitoring

---

## 🎯 Interview Relevance

This project is designed to highlight:

- **Django REST Framework expertise** (models, serializers, viewsets, permissions).  
- **Database design** with PostgreSQL.  
- **Performance optimization** via Redis caching.  
- **Security** with JWT and role-based access.  
- **Testing & CI/CD** culture (pytest, GitHub Actions).  
- **DevOps mindset** (Dockerized environment).  

You can use this project to walk through **design decisions, trade-offs, and engineering practices** in a real-world healthcare scenario.

---
