from rest_framework.response import Response
from rest_framework import generics, viewsets
from django.db.models import Q
from django.shortcuts import get_object_or_404

from ..models import Network, Organisation, Method, CustomUser, Survey
from ..serializers import NetworkSerializer, OrganisationSerializer


# Get all the available Networks of a user
class NetworkViewSet(viewsets.ModelViewSet):
    serializer_class = NetworkSerializer
   
    def get_queryset(self):
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
        return Network.objects.filter(Q(created_by=self.request.user) | Q(ispublic = True))


    
    def create(self, serializer):
        print(self.request.user)
        print('hi')
        serializer = NetworkSerializer(data=self.request.data)
        print(serializer.initial_data)
        serializer.is_valid(raise_exception=True)
        serializer.save(created_by=self.request.user)
        return Response(serializer.data)

    def partial_update(self, request, pk): # , *args, **kwargs
        print('hi')
        networkobject = get_object_or_404(Network, pk=pk)
        if "organisation_members" in request.data[0].keys():
            for instance in request.data:
                try: 
                    organisation = get_object_or_404(Organisation, name=instance['name'])
                    if networkobject.organisations.filter(name=organisation.name).exists():
                        networkobject.organisations.remove(organisation)
                    else:
                        networkobject.organisations.add(organisation)
                    print(networkobject.organisations.all())
                except:
                    pass
        else:
            for instance in request.data:
                try: 
                    method = get_object_or_404(Method, name=instance['name'])
                    if networkobject.methods.filter(name=method.name).exists():
                        networkobject.methods.remove(method)
                    else:
                        networkobject.methods.add(method)
                    print(networkobject.methods.all())
                except:
                    pass
        serializer = NetworkSerializer(networkobject)
        return Response(serializer.data)
