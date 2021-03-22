from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault

from ..models import Organisation, UserOrganisation
from .user_organisation import UserOrganisationSerializer
from .survey_response import SurveyResponseSerializer


class OrganisationSerializer(serializers.ModelSerializer):
    organisation_members = UserOrganisationSerializer(many=True, required=False)
    created_by = serializers.StringRelatedField()
    class Meta:
        model = Organisation        
        fields = ['id', 'ispublic', 'name', 'description', 'created_by', 'organisation_members']

# class MethodSerializer(serializers.ModelSerializer):
#     class Meta:
#         mode = Method

# class OrganisationResponsesSerializer(serializers.ModelSerializer):
#     methods = MethodSerializer()
#     # survey_responses = SurveyResponseSerializer(source='filtered_survey_responses', many=True, read_only=True)