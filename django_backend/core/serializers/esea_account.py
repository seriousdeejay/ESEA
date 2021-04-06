from rest_framework import serializers

from ..models import EseaAccount, Organisation, Method

class MethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Method
        fields = ['id', 'name', 'description']

class EseaAccountSerializer(serializers.ModelSerializer):
    organisation = serializers.SlugRelatedField(queryset=Organisation.objects.all(), slug_field='name')
    method = MethodSerializer(read_only=True)
    report = serializers.PrimaryKeyRelatedField(read_only=True)
    # response_rate = serializers.ReadOnlyField()
    responses = serializers.StringRelatedField(many=True)
    class Meta:
        model = EseaAccount
        fields = ['id', 'organisation', 'method', 'campaign', 'report', 'responses', 'survey_response_by_survey', 'sufficient_responses']
        # extra_kwargs = {'survey_response_by_survey':{'many': True}}

    def update(self, instance, validated_data):
        print('chec1k')
        return instance