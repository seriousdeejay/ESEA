from rest_framework import viewsets
from django.shortcuts import get_object_or_404

from ..models import Topic, Method
from ..serializers import TopicSerializer


class TopicViewSet(viewsets.ModelViewSet):
    serializer_class = TopicSerializer

    # Made a try/excepp to show Topic.objects.all() for now
    def get_queryset(self):
        try:
            return Topic.objects.filter(
                method__organisation=1,
                method__organisation__user=1,
                method=self.kwargs['method_pk']) 
        except:
            return Topic.objects.all()
    def perform_create(self, serializer):
        method = get_object_or_404(Method, pk=self.kwargs['organisation_pk']
        )
        serializer.save(method=method)