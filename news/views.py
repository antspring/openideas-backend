from rest_framework import viewsets
from .models import News
from .serializers import NewsSerializer
from rest_framework.permissions import AllowAny


# Create your views here.

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]
        return super().get_permissions()
