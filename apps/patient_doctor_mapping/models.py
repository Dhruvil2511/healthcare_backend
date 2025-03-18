from django.db import models

# Create your models here.
from apps.doctors.models import Doctor
from apps.patients.models import Patients


class PatientDoctorMapping(models.Model):
    patient = models.ForeignKey(Patients, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    assigned_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient} - {self.doctor}"
    
    class Meta:
        unique_together = ('patient', 'doctor')
