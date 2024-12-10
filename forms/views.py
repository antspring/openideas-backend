from rest_framework import viewsets
from .models import ContactForm
from .serializers import ContactFormSerializer


# Create your views here.

class ContactFormViewSet(viewsets.ModelViewSet):
    queryset = ContactForm.objects.all()
    serializer_class = ContactFormSerializer
    http_method_names = ['get', 'post', 'delete']
