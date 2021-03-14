from rest_framework import serializers

from ..models import UserOrganisation

class UserOrganisationSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.id')
    organisation = serializers.ReadOnlyField(source='organisation.id')

    class Meta:
        model = UserOrganisation
        fields = ['user', 'organisation', 'role', 'stakeholdergroups']