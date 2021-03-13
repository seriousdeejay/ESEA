from rest_framework.response import Response
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from django.shortcuts import get_object_or_404

from ..models import Network, Organisation, Method, CustomUser, Survey
from ..serializers import NetworkSerializer, OrganisationSerializer


# Get all the available Networks of a user
class NetworkViewSet(viewsets.ModelViewSet):
    serializer_class = NetworkSerializer
   
    def get_queryset(self): # First query on localhost/organisations
        print(self.request.user) 
        organisation = self.request.GET.get('organisation', None)
        excludeorganisation = self.request.GET.get('excludeorganisation', None)
        # organisationsurveys = self.request.GET.get('organisationsurveys', None)
        if organisation is not None:
            return Network.objects.filter(organisations=organisation)
        if excludeorganisation is not None:
            return Network.objects.exclude(organisations=excludeorganisation)
        # if organisationsurveys is not None:
        #     return Survey.objects.filter(method__networks__organisations=organisationsurveys)
        if self.request.user.is_authenticated:
            user = self.request.user
            return Network.objects.filter(Q(created_by=user) | Q(ispublic = True))
        # return Network.objects.all()
    
    def create(self, serializer):
        #creator = get_object_or_404(CustomUser, pk=self.request.user.id)
        serializer = NetworkSerializer(data=self.request.data)
        if serializer.is_valid():
            n = serializer.save(created_by=self.request.user) # does created_by=request.user not work?
            return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        network_object = get_object_or_404(Network, pk=self.get_object().id)
        data = request.data
        try:
            for item in data: 
                try:
                    organisation = Organisation.objects.get(id=int(item['id']), name=item['name'])
                    if network_object.organisations.filter(pk=organisation.pk).exists():
                        network_object.organisations.remove(organisation)
                    else:
                        network_object.organisations.add(organisation)
                except:
                    method = Method.objects.get(id=item['id'], name=item['name'])
                    if network_object.methods.filter(pk=method.pk).exists():
                        network_object.methods.remove(method)
                    else:
                        network_object.methods.add(method)
        except KeyError:
            pass
        network_object.save()
        serializer = NetworkSerializer(network_object)
        return Response(serializer.data)

# Get all the organisations of a network
# class NetworkOrganisationsViewSet(viewsets.ModelViewSet):
#     serializer_class = OrganisationSerializer

#     def get_queryset(self):
#         network_id = int(self.kwargs['pk'])
#         return Organisation.objects.filter(network=network_id)
