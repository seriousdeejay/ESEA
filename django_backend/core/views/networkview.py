from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from django.db.models import Q

from ..models import Network, Organisation
from ..serializers import NetworkSerializer, OrganisationSerializer


# Get all the available Networks of a user
class NetworkViewSet(viewsets.ModelViewSet):
    serializer_class = NetworkSerializer
   
    def get_queryset(self): # First query on localhost/organisations
        print(self.request.user)
        if self.request.user.is_authenticated:
            user = self.request.user
            return Network.objects.filter(Q(created_by=user) | Q(ispublic = True))
        # return Network.objects.all()
    
    def perform_create(self, serializer):
        serializer = NetworkSerializer(data=self.request.data)
        if serializer.is_valid():
            serializer.save(created_by=[self.request.user])
        return Response(serializer.data)


# Get all the organisations of a network
class NetworkOrganisationsViewSet(viewsets.ModelViewSet):
    serializer_class = OrganisationSerializer

    def get_queryset(self):
        network_id = int(self.kwargs['pk'])
        return Organisation.objects.filter(network=network_id)
