from rest_framework import serializers
from ..models import Method


class MethodSerializer(serializers.ModelSerializer):
    model = Method
    fields = '__all__'