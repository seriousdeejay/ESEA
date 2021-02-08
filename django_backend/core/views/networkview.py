from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

from ..models import Network
from ..serializers import NetworkSerializer

class NetworkViewSet(viewsets.ModelViewSet):
    serializer_class = NetworkSerializer
    queryset = Network.objects.all()