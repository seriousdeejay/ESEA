from rest_framework import serializers

from ..models import EseaAccount


class EseaAccountSerializer(serializers.ModelSerializer):
    report = serializers.PrimaryKeyRelatedField(read_only=True)
    response_rate = serializers.ReadOnlyField()

    class Meta:
        model = EseaAccount
        fields = ['id', 'organisation', 'method', 'campaign', 'report', 'responses', 'response_rate', 'sufficient_responses']

    def update(self, instance, validated_data):
        print('chec1k')
        return instance