from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


from ..models import Survey, Method
from ..serializers import SurveyOverviewSerializer, SurveyDetailSerializer


class SurveyViewSet(viewsets.ModelViewSet):
    serializer_class = SurveyOverviewSerializer
    # queryset = Survey.objects.all()

    def get_queryset(self):
        return Survey.objects.filter(method=self.kwargs['method_pk'])

    def perform__create(self, serializer):
        method = get_object_or_404(Method, pk=self.kwargs['method_pk'])
        serializer.save(method=method)
    
    def retrieve(self, request, method_pk, pk):
        survey = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = SurveyDetailSerializer(survey)

        return Response(serializer.data)

# Not really implemented!
class PublicSurveyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Survey.objects.all()
    serializer_class = SurveyOverviewSerializer
    authentication_classes = []
    permission_classes = []

    def retrieve(self, request, pk):
        survey = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = SurveyDetailSerializer(survey)

        return Response(serializer.data)