from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from django.db.models import Q
from django.shortcuts import get_object_or_404

from ..models import Network, Organisation, CustomUser
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
        creator = get_object_or_404(CustomUser, pk=self.request.user.id)
        serializer = NetworkSerializer(data=self.request.data)
        if serializer.is_valid():
            serializer.save(created_by=creator)
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        print(request)
        network_object = get_object_or_404(Network, pk=self.get_object().id)
        data = request.data
        try: 
            organisation = Organisation.objects.get(id=data['id'])
            if network_object.organisations.filter(pk=organisation.pk).exists():
                network_object.organisations.remove(organisation)
            else:
                network_object.organisations.add(organisation)
        except KeyError:
            pass
        network_object.save()
        serializer = NetworkSerializer(network_object)
        return Response(serializer.data)

# Get all the organisations of a network
class NetworkOrganisationsViewSet(viewsets.ModelViewSet):
    serializer_class = OrganisationSerializer

    def get_queryset(self):
        network_id = int(self.kwargs['pk'])
        return Organisation.objects.filter(network=network_id)
