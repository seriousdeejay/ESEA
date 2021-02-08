from rest_framework import serializers
from ..models import Organisation


class OrganisationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organisation        
        fields = ('id', 'ispublic', 'name', 'description', 'creator', 'participants', 'title', 'content')
