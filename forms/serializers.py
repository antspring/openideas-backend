from rest_framework import serializers
from .models import ContactForm


class ContactFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactForm
        fields = ['id', 'full_name', 'organization', 'email', 'phone_number', 'message', 'created_at']
