from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault

from ..models import Organisation, UserOrganisation
from .user_organisation import UserOrganisationSerializer


class OrganisationSerializer(serializers.ModelSerializer):
    organisation_members = UserOrganisationSerializer(many=True, required=False)
    created_by = serializers.StringRelatedField()
    class Meta:
        model = Organisation        
        fields = ['id', 'ispublic', 'name', 'description', 'created_by', 'organisation_members']
