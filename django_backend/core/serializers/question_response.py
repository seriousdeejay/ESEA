from rest_framework import serializers

from ..models import QuestionResponse, AnswerList, QuestionOption
from .question_option import QuestionOptionSerializer

class QuestionResponseSerializer(serializers.ModelSerializer):
    #values = QuestionOptionSerializer(many=True)
    values = serializers.SlugRelatedField(queryset=QuestionOption.objects.all(), many=True, slug_field='text')

    class Meta:
        model = QuestionResponse
        fields = ['id', 'direct_indicator_id', 'values']
        extra_kwargs = {'id': {'read_only': False, 'required': True}}