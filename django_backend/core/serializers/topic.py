from rest_framework import serializers
from ..models import Topic


class TopicSerializer(serializers.ModelSerializer):
    # parent_topic = serializers.PrimaryKeyRelatedField(many=False)
    method = serializers.PrimaryKeyRelatedField(read_only=True)
    parent_topic_name = serializers.StringRelatedField(source='parent_topic', read_only=True)

    class Meta:
        model = Topic
        fields = ('id', 'name', 'description', 'parent_topic', 'parent_topic_name', 'method', 'questions')
        depth = 2
        # read_only_fields = ['Method']