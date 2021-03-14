from rest_framework.response import Response
# from rest_framework import generics
# from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from django.db.models import Q
from django.shortcuts import get_object_or_404

from ..models import Organisation, CustomUser, UserOrganisation
from ..serializers import OrganisationSerializer


class OrganisationViewSet(viewsets.ModelViewSet):
    serializer_class = OrganisationSerializer
   
    def get_queryset(self): # First query on localhost/organisations
        network = self.request.GET.get('network', None)
        excludenetwork = self.request.GET.get('excludenetwork', None)
        if network is not None:
            return Organisation.objects.filter(networks=network)
        if excludenetwork is not None:
            return Organisation.objects.exclude(networks=excludenetwork)
        if self.request.user.is_authenticated:
            user = self.request.user
            print(self.request.user)
            return Organisation.objects.filter(Q(creator=user) | Q(ispublic = True))
        # return Organisation.objects.all()
    
    # Need to put perform_create on the userorganisation model (?)
    # def create(self, serializer):
        
    #     serializer = OrganisationSerializer(data=self.request.data)
    #     if serializer.is_valid():
    #         serializer.save(creator=self.request.user)
    #         O = Organisation.objects.get(id=serializer.data['id'])
    #         u = UserOrganisation.objects.create(user=self.request.user, organisation=O)
    #         return Response(serializer.data)
    # #     creator = get_object_or_404(CustomUser, pk=self.request.user.id)
    # #     user_organisation = UserOrganisation.objects.create(user=self.request.user, organisation=)

    # #     serializer = OrganisationSerializer(data=self.request.data)
    # #     if serializer.is_valid():
    # #         serializer.save(creator=creator, organisation_participants=[creator])
    # #         return Response(serializer.data)
    #     return Response({"Nothing uploaded"})

    def partial_update(self, request, *args, **kwargs):
        organisation_object = get_object_or_404(Organisation, pk=self.get_object().id)
        data = request.data
        try:
            for user in data:
                user = CustomUser.objects.get(id = user['id'])
                if organisation_object.participants.filter(pk=user.pk).exists():                    
                    organisation_object.participants.remove(user)
                else:
                    organisation_object.participants.add(user)
        except KeyError:
            pass
        organisation_object.save()
        serializer = OrganisationSerializer(organisation_object)
        return Response(serializer.data)

    # Add user():

    # Remove user():

# Get all the participants of an organisation
# class OrganisationParticipantsViewSet(viewsets.ModelViewSet):
#     serializer_class = UserSerializer

#     def get_queryset(self):
#         organisation_id = int(self.kwargs['pk'])
#         return CustomUser.objects.filter(accessible_organisations=organisation_id)


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