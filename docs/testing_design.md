# API Testing Design and Implementation

This document describes the approach and implementation for testing the Patient Health Records API.

## Testing Approach
- All API endpoints are tested using Django REST Framework's `APITestCase`.
- Tests cover CRUD operations for each core entity: Patient, Doctor, Appointment, Prescription, and HealthRecord.
- Edge cases, such as invalid data and partial updates, are included.
- Tests are located in `records/tests.py`.

## Test Coverage
- **Patient**: Create, retrieve, update, delete
- **Doctor**: Create, retrieve, update, delete
- **Appointment**: Create, retrieve, update, delete
- **Prescription**: Create, retrieve, update, delete
- **HealthRecord**: Create, retrieve, update, delete

## Tools and Libraries
- `pytest` and `pytest-django` for running tests
- `rest_framework.test.APIClient` for making API requests
- Django's test database for isolation and repeatability

## Running Tests
1. Ensure dependencies are installed:
   ```
   pip install pytest pytest-django
   ```
2. Ensure `pytest.ini` is present in the project root with the correct settings.
3. Run database migrations:
   ```
   python manage.py migrate
   ```
4. Run the test suite:
   ```
   pytest
   ```

## Notes
- All tests are isolated and use the test database.
- The suite can be extended to cover authentication, permissions, and edge cases as the project evolves.
