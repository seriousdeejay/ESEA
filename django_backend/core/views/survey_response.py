from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
# from secrets import token_urlsafe

from ..models import (Survey, SurveyResponse, UserOrganisation)
from ..serializers import (SurveyResponseSerializer) #, SurveyResponseCalculationSerializer
# from ..utils import calculate_indicators, map_responses_by_indicator


class SurveyResponseViewSet(viewsets.ModelViewSet):
    serializer_class = SurveyResponseSerializer

    def get_queryset(self):
        return SurveyResponse.objects.filter(survey__method=self.kwargs['method_pk']), survey=self.kwargs['survey_pk']

    def perform_create(self, serializer):
        user_organisation = get_object_or_404(UserOrganisation, participant=self.request.user, organisation=self.kwargs['organisation_pk'])
        survey = get_object_or_404(Survey, pk=self.kwargs['survey_pk'])
        serializer.save(survey=survey, user_organisation=user_organisation)