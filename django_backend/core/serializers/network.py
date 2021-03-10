from rest_framework import serializers

from ..models import Network


class NetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Network
        fields = ['id', 'ispublic', 'name', 'description', 'created_by', 'organisations', 'methods']
        depth = 1