from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .models import ContactForm
from .serializers import ContactFormSerializer


# Create your views here.

class ContactFormViewSet(viewsets.ModelViewSet):
    queryset = ContactForm.objects.all()
    serializer_class = ContactFormSerializer
    http_method_names = ['get', 'post', 'delete']

    def get_permissions(self):
        if self.action in ['list', 'retrieve', 'create']:
            return [AllowAny()]
        return super().get_permissions()
