from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault

from ..models import Organisation, UserOrganisation
from .user_organisation import UserOrganisationSerializer


class OrganisationSerializer(serializers.ModelSerializer):
    # organisation_participants = UserOrganisationSerializer(many=True)
    class Meta:
        model = Organisation        
        fields = ['name', 'description']
        # extra_kwargs = {'participants': {'required': False}, 'organisation_participants' : {'required': False}}
    
    # def create(self, validated_data):
    # #     # userorganisation = validated_data.pop('organisation_participants')
    # #     print(self.request.user)
    #     organisation = Organisation.objects.create(self, **validated_data)
    # #     userorganisation = UserOrganisation.objects.create(user=user, organisation=organisation)
    #     return organisation