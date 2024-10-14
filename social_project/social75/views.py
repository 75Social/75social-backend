from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import HelloSerializer
from .models import HelloWorld

class HelloViewSet(viewsets.ModelViewSet):
    queryset = HelloWorld.objects.all()
    serializer_class = HelloSerializer