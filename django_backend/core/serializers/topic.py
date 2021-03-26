from rest_framework import serializers

from ..models import Topic


class TopicSerializer(serializers.ModelSerializer):
    parent_topic_name = serializers.StringRelatedField(source='parent_topic', read_only=True)
    method = serializers.StringRelatedField()

    class Meta:
        model = Topic
        fields = ('id', 'parent_topic', 'name', 'description', 'parent_topic_name', 'method', 'questions')
        read_only_fields = ['Method']