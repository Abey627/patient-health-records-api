from django.urls import path
from . import views

urlpatterns = [
    # Patient endpoints
    path('patients/', views.PatientListCreateView.as_view(), name='patient-list-create'),
    path('patients/<int:pk>/', views.PatientRetrieveUpdateDestroyView.as_view(), name='patient-detail'),

    # Doctor endpoints
    path('doctors/', views.DoctorListCreateView.as_view(), name='doctor-list-create'),
    path('doctors/<int:pk>/', views.DoctorRetrieveUpdateDestroyView.as_view(), name='doctor-detail'),

    # HealthRecord endpoints
    path('health-records/', views.HealthRecordListCreateView.as_view(), name='healthrecord-list-create'),
    path('health-records/<int:pk>/', views.HealthRecordRetrieveUpdateDestroyView.as_view(), name='healthrecord-detail'),
]
