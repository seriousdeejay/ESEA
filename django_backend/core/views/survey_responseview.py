from rest_framework import viewsets
from rest_framework.decorators import action, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from django.shortcuts import get_object_or_404
from secrets import token_urlsafe

from ..models import (Survey, SurveyResponse, QuestionResponse, DirectIndicator, Respondent)
from ..serializers import (SurveyResponseSerializer, QuestionResponseSerializer, SurveyResponseCalculationSerializer)
from ..utils import map_responses_by_indicator, calculate_indicators

class BaseModelViewSet(viewsets.ModelViewSet):
    queryset = ''
    serializer_class = ''
    permission_classes = (AllowAny,)

    # Refer to https://stackoverflow.com/a/35987077/1677041
    permission_classes_by_action = {
        'create': permission_classes,
        'list': permission_classes,
        'retrieve': permission_classes,
        'update': permission_classes,
        'destroy': permission_classes,
    }

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            if self.action:
                action_func = getattr(self, self.action, {})
                action_func_kwargs = getattr(action_func, 'kwargs', {})
                permission_classes = action_func_kwargs.get('permission_classes')
            else:
                permission_classes = None

            return [permission() for permission in (permission_classes or self.permission_classes)]

class SurveyResponseViewSet(BaseModelViewSet):
    serializer_class = SurveyResponseSerializer
    lookup_field = 'token'
    permission_classes_by_action = {
        'create': (IsAuthenticated,),
        'list': (AllowAny,),
        'retrieve': (AllowAny,),
        'update': (AllowAny,),
        'destroy': (IsAuthenticated,),
        'all': (IsAuthenticated,)
    }
    permission_classes = [AllowAny,]
    def get_queryset(self):
        print('hi')
        organisation = self.request.GET.get('organisation', None)
        if organisation is not None:
            # could also get UserOrganisation and add it to the filter
            return SurveyResponse.objects.filter(survey__method=self.kwargs['method_pk'], user_organisation__organisation=organisation, finished=True)
        return SurveyResponse.objects.filter(survey__method=self.kwargs['method_pk'], finished=True)
        return SurveyResponse.objects.filter(survey__method=self.kwargs['method_pk'], survey=self.kwargs['survey_pk'])

    # def create(self, serializer, method_pk, survey_pk, organisation_pk):
        
    #     print('it exists!')
    #     return Response('something')
    
    
    def retrieve(self, request, method_pk, survey_pk, organisation_pk, token):
        print(self.request.user)
        surveyresponse = get_object_or_404(SurveyResponse, token=token)
        print(surveyresponse)
        serializer = SurveyResponseSerializer(surveyresponse)
        return Response(serializer.data) 

    def create(self, request, method_pk, survey_pk, organisation_pk):
        surveyresponse = SurveyResponse.objects.create(survey=request.data['survey'], user_organisation=request.data['user_organisation'])
        serializer = SurveyResponseSerializer(surveyresponse)
        return Response(serializer.data)
    
    def update(self, request, organisation_pk, method_pk, survey_pk, token, **kwargs):
        surveyresponse = get_object_or_404(SurveyResponse, token=token)
        serializer = SurveyResponseSerializer(surveyresponse, data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
        # direct_indicator = get_object_or_404(DirectIndicator, pk=pk, topic__method=method_pk)
        # serializer = DirectIndicatorSerializer(direct_indicator, data=request.data)
    

    @action(detail=False, methods=['get'])
    # @permission_classes(AllowAny,)
    def all(self, request, method_pk, survey_pk, organisation_pk):
        if self.request.user.is_authenticated:
            respondents = Respondent.objects.filter(organisation=organisation_pk, response__survey=survey_pk)
            responses = SurveyResponse.objects.filter(respondent__organisation=organisation_pk, survey = survey_pk, finished=True)

            question_responses = QuestionResponse.objects.filter(survey_response__respondent__organisation= organisation_pk, survey_response__survey=survey_pk, survey_response__finished=True)
            # indirect_indicators = IndirectIndicator.objects.filter(topic__method=method_pk)
            direct_indicators = DirectIndicator.objects.filter(surveys=survey_pk)
            
            for item in question_responses:
                s = QuestionResponseSerializer(item)
            map_responses_by_indicator(direct_indicators, question_responses)
            for di in direct_indicators:
                print(di.key)
            # serializer = SurveyResponseCalculationSerializer(direct_indicators, many=True)
            indicators = calculate_indicators(direct_indicators)
            #serializer = SurveyResponseCalculationSerializer(indicators.values(), many=True)
            return Response(
                {
                    "respondents": len(respondents),
                    "responses": len(responses.filter(finished=True)),
                    "indicators": indicators,
                }
            )
        return Response({})
        

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