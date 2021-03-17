from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from secrets import token_urlsafe

from ..models import (Survey, SurveyResponse, QuestionResponse, UserOrganisation, DirectIndicator)
from ..serializers import (SurveyResponseSerializer, QuestionResponseSerializer) #, SurveyResponseCalculationSerializer
from ..utils import map_responses_by_indicator # calculate_indicators,


class SurveyResponseViewSet(viewsets.ModelViewSet):
    serializer_class = SurveyResponseSerializer

    def get_queryset(self):
        organisation = self.request.GET.get('organisation', None)
        if organisation is not None:
            # could also get UserOrganisation and add it to the filter
            return SurveyResponse.objects.filter(survey__method=self.kwargs['method_pk'], survey=self.kwargs['survey_pk'], user_organisation__organisation=organisation, user_organisation__user=self.request.user)
        return SurveyResponse.objects.filter(survey__method=self.kwargs['method_pk'], survey=self.kwargs['survey_pk'])

    def perform_create(self, serializer):
        user_organisation = get_object_or_404(UserOrganisation, user=self.request.user, organisation=self.kwargs['organisation_pk']) # organisation=self.kwargs['organisation_pk']
        survey = get_object_or_404(Survey, pk=self.kwargs['survey_pk'])
        print(user_organisation, survey)
        serializer.save(survey=survey, user_organisation=user_organisation)
    
    @action(detail=False, methods=['get'])
    def all(self, request, method_pk, survey_pk, organisation_pk):
        
        all_respondents = SurveyResponse.objects.filter(survey__method=method_pk, survey=survey_pk)

        question_responses = QuestionResponse.objects.filter(survey_response__survey__method=method_pk, survey_response__survey=survey_pk, survey_response__finished=True)
        # indirect_indicators = IndirectIndicator.objects.filter(topic__method=method_pk)
        direct_indicators = DirectIndicator.objects.filter(survey=survey_pk)
        print(direct_indicators)
        for item in question_responses:
            s = QuestionResponseSerializer(item)
            print(s.data)
        map_responses_by_indicator(direct_indicators, question_responses)
        #indicators = calculate_indicators(indirect_indicators, direct_indicators)
        #serializer = SurveyResponseCalculationSerializer(indicators.values(), many=True)
        return Response(
            {
                "all_respondents": len(all_respondents),
                "respondents": len(all_respondents.filter(finished=True)),
                #"indicators": serializer.data,
            }
        )
        

#     @action(detail=True, methods=["get"])
#     def calculations(self, request, organization_pk, method_pk, survey_pk, pk):
#         survey_response = get_object_or_404(self.get_queryset(), pk=pk)
#         indirect_indicators = IndirectIndicator.objects.filter(
#             topic__method=method_pk,
#         )
#         direct_indicators = survey_response.survey.questions.all()
#         question_responses = survey_response.question_responses.all()

#         map_responses_by_indicator(
#             direct_indicators, question_responses,
#         )
#         indicators = calculate_indicators(
#             indirect_indicators, direct_indicators,
#         )
#         serializer = SurveyResponseCalculationSerializer(
#             indicators.values(), many=True
#         )
#         return Response(serializer.data)


# class PublicSurveyResponseViewset(viewsets.ModelViewSet):
#     serializer_class = SurveyResponseSerializer
#     authentication_classes = []
#     permission_classes = []

#     def get_queryset(self):
#         token = self.request.query_params.get("token")
#         return SurveyResponse.objects.filter(
#             survey=self.kwargs["survey_pk"],
#             user_organization=None,
#             token=token,
#         )

#     def perform_create(self, serializer):
#         token = self.request.query_params.get("token", token_urlsafe())
#         survey = get_object_or_404(Survey, pk=self.kwargs["survey_pk"])
#         serializer.save(survey=survey, token=token)