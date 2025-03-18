from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import PatientDoctorMapping
from .serializers import PatientDoctorMappingSerializer
from rest_framework.response import Response


# Create your views here.
class PatientDoctorMappingViewSet(viewsets.ModelViewSet):
    queryset = PatientDoctorMapping.objects.all()
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [IsAuthenticated]

    def get_doctors_for_patient(self, request, patient_id):
        mappings = PatientDoctorMapping.objects.filter(patient_id=patient_id)
        serializer = PatientDoctorMappingSerializer(mappings, many=True)
        mappedArray = serializer.data
        doctors = []
        for mapping in mappedArray:
            doctors.append(
                {"doctor": mapping["doctor"], "doctor_name": mapping["doctor_name"]}
            )
        return Response(doctors)
