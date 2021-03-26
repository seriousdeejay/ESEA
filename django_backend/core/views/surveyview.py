from rest_framework import viewsets, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


from ..models import Survey, Method, UserOrganisation, Organisation, SurveyResponse
from ..serializers import SurveyOverviewSerializer, SurveyDetailSerializer, UserOrganisationSerializer


class SurveyViewSet(viewsets.ModelViewSet):
    serializer_class = SurveyOverviewSerializer

    def get_queryset(self):
        organisation = self.request.GET.get('organisation', None)
        completedbyorganisation = self.request.GET.get('completedbyorganisation', None)
        if organisation or completedbyorganisation is not None:
            try:
                org = Organisation.objects.get(id=organisation or completedbyorganisation)
                print(org)
                
                # userorganisation = UserOrganisation.objects.get(user=self.request.user, organisation=org)
                #print(userorganisation)
            except:
                return Survey.objects.none()
            #ids = userorganisation.stakeholdergroups.values_list('id', flat=True)
            #print(ids)
            if organisation:
                return Survey.objects.filter(method=self.kwargs['method_pk'])
                # return Survey.objects.filter(method__networks__organisations=org, stakeholder_groups__pk__in=ids).exclude(responses__in=SurveyResponse.objects.filter(user_organisation=userorganisation, finished=True))
            if completedbyorganisation:
                return Survey.objects.filter(method__networks__organisations=org, stakeholder_groups__pk__in=ids, responses__user_organisation=userorganisation, responses__finished=True).distinct() 
        return Survey.objects.filter(method=self.kwargs['method_pk'])
    
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