from django.urls import path
from . import views

urlpatterns = [
    # Patient endpoints
    path('patients/', views.PatientListCreateView.as_view(), name='patient-list-create'),
    path('patients/<int:pk>/', views.PatientRetrieveUpdateDestroyView.as_view(), name='patient-detail'),

    # Doctor endpoints
    path('doctors/', views.DoctorListCreateView.as_view(), name='doctor-list-create'),
    path('doctors/<int:pk>/', views.DoctorRetrieveUpdateDestroyView.as_view(), name='doctor-detail'),

    # Appointment endpoints
    path('appointments/', views.AppointmentListCreateView.as_view(), name='appointment-list-create'),
    path('appointments/<int:pk>/', views.AppointmentRetrieveUpdateDestroyView.as_view(), name='appointment-detail'),

    # Prescription endpoints
    path('prescriptions/', views.PrescriptionListCreateView.as_view(), name='prescription-list-create'),
    path('prescriptions/<int:pk>/', views.PrescriptionRetrieveUpdateDestroyView.as_view(), name='prescription-detail'),

    # HealthRecord endpoints
    path('health-records/', views.HealthRecordListCreateView.as_view(), name='healthrecord-list-create'),
    path('health-records/<int:pk>/', views.HealthRecordRetrieveUpdateDestroyView.as_view(), name='healthrecord-detail'),
]
