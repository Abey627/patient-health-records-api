# Authentication & Authorization Design

This document summarizes how authentication and authorization are designed and implemented in the Patient Health Records API.

---

## Authentication

- **JWT-based Authentication**: The API uses JWT (JSON Web Token) authentication via the `djangorestframework-simplejwt` package.
- **Token Endpoints**: Users obtain tokens by POSTing their username and password to `/api/token/`. Tokens can be refreshed at `/api/token/refresh/`.
- **DRF Settings**: In `settings.py`, the default authentication class is set to JWT (`rest_framework_simplejwt.authentication.JWTAuthentication`), and all endpoints require authentication by default (`IsAuthenticated`).

## User Roles

- **UserProfile Model**: Each user has a `UserProfile` linked to Django’s built-in `User` model. The profile includes a `role` field, which can be either `doctor` or `patient`.
- **Automatic Profile Creation**: Profiles are automatically created for new users via Django signals.
- **Role Assignment**: Roles can be assigned or changed by admins in the Django admin interface.

## Authorization (Permissions)

- **Custom Permission Classes**: In `records/permissions.py`, two custom classes are defined:
	- `IsDoctor`: Only allows access to users whose profile role is `doctor`.
	- `IsPatient`: Only allows access to users whose profile role is `patient`.
- **Permission Mixins**: In `records/views.py`, mixins (`DoctorPermissionMixin`, `PatientPermissionMixin`) are used to apply these permissions to views.
- **Role-based Access Control**: API views for patients, doctors, appointments, prescriptions, and health records use these mixins to restrict access based on user role.
	- Example: Only doctors can access prescription endpoints; only patients can access appointment endpoints.
- **Enforcement in Tests**: Test cases in `records/tests.py` verify that endpoints enforce both authentication and correct role-based permissions (e.g., patients cannot access doctor-only endpoints).

## Admin and Registration

- **Admin Interface**: Admins can create users and assign roles.
- **Extensible Registration**: The system can be extended to allow self-service signup with role selection.

## References

- [Django REST Framework SimpleJWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)
- [DRF Permissions](https://www.django-rest-framework.org/api-guide/permissions/)

---

**Summary:**

Authentication is handled via JWT tokens, and authorization is enforced using custom permission classes that check the user’s role. All endpoints require authentication, and access is restricted based on whether the user is a doctor or patient, as defined in their profile.
