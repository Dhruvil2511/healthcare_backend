from rest_framework import serializers
from .models import Doctor

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id', 'name', 'experience_years', 'phone', 'specialization', 'created_at', 'updated_at']  
        

