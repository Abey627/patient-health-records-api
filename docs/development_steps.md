
# Project Development Steps

This document outlines the recommended steps for developing the Patient Health Records API using Django and Django REST Framework. Use the checklist below to mark progress:

## Development Checklist

- [x] Define data models in `records/models.py` (e.g., Patient, HealthRecord)
- [x] Register models in `records/admin.py` for admin management
- [x] Implement serializers and API views in `records/views.py` using Django REST Framework
- [x] Add URL patterns for API endpoints in `records/urls.py` and include in `phrapi/urls.py`
- [x] Auto-document API endpoints using drf-spectacular (Scalar)
- [ ] Write unit tests in `records/tests.py` for models and API endpoints
- [ ] Update documentation in `README.md` with setup and API usage
- [ ] Run migrations to create database tables (`python manage.py makemigrations` and `python manage.py migrate`)

Refer to this checklist as you progress through development. Tick off each item as you complete it.
