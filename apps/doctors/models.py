from django.core.validators import RegexValidator
from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=255)
    experience_years = models.IntegerField()
    
    phone_validator = RegexValidator(
        regex=r'^\d{10}$',
        message="Phone number must be exactly 10 digits."
    )
    phone = models.CharField(
        max_length=10, 
        unique=True, 
        validators=[phone_validator]
    )
    
    specialization = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
