from rest_framework.response import Response
from rest_framework import viewsets
from django.db.models import Q, Prefetch
from django.shortcuts import get_object_or_404

from ..models import Organisation, CustomUser, UserOrganisation, StakeholderGroup, SurveyResponse
from ..serializers import OrganisationSerializer


class OrganisationViewSet(viewsets.ModelViewSet):
    serializer_class = OrganisationSerializer
   
    def get_queryset(self):
        network = self.request.GET.get('network', None)
        excludenetwork = self.request.GET.get('excludenetwork', None)
        method = self.request.GET.get('method', None)
        excludemethod = self.request.GET.get('excludemethod', None)
        if network is not None:
            if method is not None:
                print('It Works!')
                return Organisation.objects.filter(networks=network, methods=method)
                #serializer_class = OrganisationResponsesSerializer
                #return Organisation.objects.prefetch_related(Prefetch('methods.surveys.responses', queryset=SurveyResponse.objects.filter(survey__method=method, survey__method__networks=network), to_attr='filtered_survey_responses'))
            if excludemethod is not None:
                print('check')
                return Organisation.objects.filter(networks=network).exclude(methods=excludemethod)
            return Organisation.objects.filter(networks=network)
        if excludenetwork is not None:
            return Organisation.objects.exclude(networks=excludenetwork)
        return Organisation.objects.filter(Q(created_by=self.request.user) | Q(ispublic = True))
    
    def create(self, serializer):
        print('yeha')
        serializer = OrganisationSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        organisation = serializer.save(created_by=self.request.user)
        userorganisation = UserOrganisation.objects.create(user=self.request.user, organisation=organisation)
        stakeholdergroup = StakeholderGroup.objects.get(name="Employee")
        userorganisation.stakeholdergroups.add(stakeholdergroup)
        userorganisation.save()
        print('check')
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        organisation_object = get_object_or_404(Organisation, pk=self.get_object().id)
        data = request.data
        try:
            for user in data:
                user = CustomUser.objects.get(id = user['id'])
                if organisation_object.members.filter(pk=user.pk).exists():                    
                    organisation_object.members.remove(user)
                else:
                    organisation_object.members.add(user)
        except KeyError:
            pass
        organisation_object.save()
        serializer = OrganisationSerializer(organisation_object)
        return Response(serializer.data)