from rest_framework import viewsets, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


from ..models import Survey, Method, UserOrganisation, Organisation
from ..serializers import SurveyOverviewSerializer, SurveyDetailSerializer, UserOrganisationSerializer


class SurveyViewSet(viewsets.ModelViewSet):
    serializer_class = SurveyOverviewSerializer

    def get_queryset(self):
        organisation = self.request.GET.get('organisation', None)
        if organisation is not None:
            try:
                organisation = Organisation.objects.get(id=organisation)
                userorganisation = UserOrganisation.objects.get(user=self.request.user, organisation=organisation)
            except:
                return Survey.objects.none()
            ids = userorganisation.stakeholdergroups.values_list('id', flat=True)
            return Survey.objects.filter(method__networks__organisations=organisation, stakeholder_groups__pk__in=ids)
        # return Survey.objects.filter(method=self.kwargs['method_pk'])
    
    def retrieve(self, request, method_pk, pk):
        survey = get_object_or_404(self.get_queryset(), pk=pk)
        print(survey)
        serializer = SurveyDetailSerializer(survey)
        return Response(serializer.data) 

# Not really implemented!
class PublicSurveyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Survey.objects.all()
    serializer_class = SurveyOverviewSerializer
    authentication_classes = []
    permission_classes = []

    def retrieve(self, request, pk):
        survey = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = SurveyDetailSerializer(survey)

        return Response(serializer.data)