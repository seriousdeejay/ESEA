from rest_framework.response import Response
# from rest_framework import generics
# from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from django.db.models import Q

from ..models import Organisation, CustomUser
from ..serializers import OrganisationSerializer, UserSerializer


# Get all the available organisations of a user
class OrganisationViewSet(viewsets.ModelViewSet):
    serializer_class = OrganisationSerializer
   
    def get_queryset(self): # First query on localhost/organisations
        if self.request.user.is_authenticated:
            user = self.request.user
            print(self.request.user)
            return Organisation.objects.filter(Q(creator=user) | Q(ispublic = True))
        # return Organisation.objects.all()
    

# Get all the participants of an organisation
class OrganisationParticipantsViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        organisation_id = int(self.kwargs['pk'])
        return CustomUser.objects.filter(accessible_organisations=organisation_id)


# class OrganisationView(generics.ListCreateAPIView): # RetrieveAPIView):
#     # permission_classes = (IsAuthenticated,) # Authentication required
#     queryset = Organisation.objects.all()
#     serializer_class = OrganisationSerializer


# class OrganisationDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Organisation.objects.all()
#     serializer_class = OrganisationSerializer


# class OrganisationViewSet(viewsets.ModelViewSet):
#     serializer_class = OrganisationSerializer
#     queryset = Organisation.objects.all()