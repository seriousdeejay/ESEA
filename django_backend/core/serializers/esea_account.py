from rest_framework import serializers

from ..models import EseaAccount


class EseaAccountSerializer(serializers.ModelSerializer):
    report = serializers.PrimaryKeyRelatedField(read_only=True)
    response_rate = serializers.ReadOnlyField()

    class Meta:
        model = EseaAccount
        fields = ['id', 'organisation', 'method', 'campaign', 'report', 'responses', 'response_rate']