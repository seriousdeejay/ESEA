from rest_framework.response import Response
from rest_framework import viewsets
from django.db.models import Q
from django.shortcuts import get_object_or_404

from ..models import Organisation, CustomUser, UserOrganisation, StakeholderGroup
from ..serializers import OrganisationSerializer


class OrganisationViewSet(viewsets.ModelViewSet):
    serializer_class = OrganisationSerializer
   
    def get_queryset(self):
        network = self.request.GET.get('network', None)
        excludenetwork = self.request.GET.get('excludenetwork', None)
        if network is not None:
            return Organisation.objects.filter(networks=network)
        if excludenetwork is not None:
            return Organisation.objects.exclude(networks=excludenetwork)
        return Organisation.objects.filter(Q(created_by=self.request.user) | Q(ispublic = True))
    
    def create(self, serializer):
        serializer = OrganisationSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        organisation = serializer.save(created_by=self.request.user)
        userorganisation = UserOrganisation.objects.create(user=self.request.user, organisation=organisation)
        stakeholdergroup = StakeholderGroup.objects.get(name="Employee")
        userorganisation.stakeholdergroups.add(stakeholdergroup)
        userorganisation.save()

        return Response(serializer.data)

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