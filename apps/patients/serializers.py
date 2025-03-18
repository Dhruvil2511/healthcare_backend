from rest_framework import serializers
from .models import Patients


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patients
        fields = ['id', 'first_name', 'last_name', 'dob', 'gender', 'phone', 'medical_history']

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)  