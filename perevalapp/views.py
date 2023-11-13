from rest_framework import viewsets
from .models import *
from rest_framework.response import Response
from .serializers import *


class PerevalViewSet(viewsets.ModelViewSet):
    queryset = Pereval.objects.all()
    serializer_class = PerevalSerializer