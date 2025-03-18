from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .models import Doctor
from .serializers import DoctorSerializer

# Create your views here.


class DoctorViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()

