from rest_framework import serializers

from ..models import UserOrganisation

class UserOrganisationSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.id')
    organisation = serializers.ReadOnlyField(source='organisation.id')
    user = serializers.StringRelatedField()
    organisation = serializers.StringRelatedField()
    stakeholdergroups = serializers.StringRelatedField(many=True)

    class Meta:
        model = UserOrganisation
        fields = ['user', 'organisation', 'role', 'stakeholdergroups']