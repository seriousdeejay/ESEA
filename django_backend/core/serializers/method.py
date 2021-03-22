from rest_framework import serializers

from ..models import Method, Survey, SurveyResponse
from .user_organisation import UserOrganisationSerializer


class ResponsesSerializer(serializers.ModelSerializer):
    user_organisation = UserOrganisationSerializer()
    class Meta:
        model = SurveyResponse
        fields = '__all__'

class SurveySerializer(serializers.ModelSerializer):
    responses = ResponsesSerializer(many=True, read_only=True)
    class Meta:
        model = Survey
        fields = ['id', 'name', 'description', 'rate', 'anonymous', 'questions', 'stakeholder_groups', 'responses']

class MethodSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField()
    #surveyresponses = SurveyResponseSerializer(source='responses', read_only=True)
    surveys = SurveySerializer(many=True, read_only=True)
    class Meta:
        model = Method
        fields = ['id', 'ispublic', 'name', 'description', 'created_by', 'networks', 'organisations', 'surveys']