from rest_framework import serializers
from ..models import Method


class MethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Method
        fields = ('ispublic', 'name', 'description', 'organisations')