from rest_framework import serializers

from ..models import Network


class NetworkSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField()
    organisations = serializers.StringRelatedField(many=True, required=False)
    methods = serializers.StringRelatedField(many=True, required=False)

    class Meta:
        model = Network
        fields = ['id', 'ispublic', 'name', 'description', 'created_by', 'organisations', 'methods']
        #depth = 1