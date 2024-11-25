from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.

class ContactForm(models.Model):
    full_name = models.CharField(max_length=100)
    organization = models.CharField(max_length=100, null=True)
    email = models.EmailField()
    phone_number = PhoneNumberField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)