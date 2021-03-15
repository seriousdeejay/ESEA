from rest_framework import serializers

from ..models import Method


class MethodSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField()
    
    class Meta:
        model = Method
        fields = ['id', 'ispublic', 'name', 'description', 'created_by']