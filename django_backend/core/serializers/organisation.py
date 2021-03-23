from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault

from ..models import Organisation, UserOrganisation, SurveyResponse
from .user_organisation import UserOrganisationSerializer
from .survey_response import SurveyResponseSerializer


class OrganisationSerializer(serializers.ModelSerializer):
    # organisation_members = UserOrganisationSerializer(many=True, required=False)
    created_by = serializers.StringRelatedField()
    organisation_members = UserOrganisationSerializer(many=True)
    class Meta:
        model = Organisation        
        fields = ['id', 'ispublic', 'name', 'description', 'created_by', 'organisation_members']

class FilteredListSerializer(serializers.ListSerializer):

    def to_representation(self, data):
        data = data.filter(user=self.context['request'].user, edition__hide=False)
        return super(FilteredListSerializer, self).to_representation(data)

class SurveyResponseSerializer2(serializers.ModelSerializer):
    class Meta:
        model = SurveyResponse
        fields = ['id', 'finished', 'survey']

class UserOrganisationSerializer2(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    stakeholdergroups = serializers.StringRelatedField(many=True)
    survey_responses = SurveyResponseSerializer2(many=True)

    class Meta:
        model = UserOrganisation
        fields = ['id', 'user', 'organisation', 'stakeholdergroups', 'survey_responses']


class OrganisationSerializer2(serializers.ModelSerializer):
    organisation_members = UserOrganisationSerializer2(many=True, source="relevant_survey_responses")

    class Meta:
        model = Organisation
        fields = ['id', 'name', 'description', 'created_by', 'members', 'organisation_members']
# class MethodSerializer(serializers.ModelSerializer):
#     class Meta:
#         mode = Method

# class OrganisationResponsesSerializer(serializers.ModelSerializer):
#     methods = MethodSerializer()
#     # survey_responses = SurveyResponseSerializer(source='filtered_survey_responses', many=True, read_only=True)