from rest_framework import serializers
from ..models import Organisation


class OrganisationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organisation        
        fields = '__all__' # ('id', 'ispublic', 'name', 'description', 'creator', 'participants')
        depth = 1