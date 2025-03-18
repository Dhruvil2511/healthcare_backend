from django.urls import path
from .views import PatientDoctorMappingViewSet

urlpatterns = [
    path(
        "",
        PatientDoctorMappingViewSet.as_view({"get": "list", "post": "create"}),
        name="patient_doctor_mapping-list-create",
    ),
    path(
        "<int:pk>/",
        PatientDoctorMappingViewSet.as_view({"get": "retrieve", "delete": "destroy"}),
        name="patient_doctor_mapping-retrieve-delete",
    ),
    path(
        "doctors/<int:patient_id>/",
        PatientDoctorMappingViewSet.as_view({"get": "get_doctors_for_patient"}),
        name="patient-doctor-mappings",
    ),
]
