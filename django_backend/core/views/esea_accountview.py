from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from ..models import EseaAccount
from ..serializers import EseaAccountSerializer

class EseaAccountViewSet(viewsets.ModelViewSet):
    serializer_class = EseaAccountSerializer

    def get_queryset(self):
        return EseaAccount.objects.all()

    def update(self, request, network_pk, campaign_pk, pk):
        esea_account = get_object_or_404(EseaAccount, pk=pk)
        print(esea_account.sufficient_response_rate()) # Maybe i have to put this in the serializer update method? If sufficient_response_rate gets returned a report can be created

        return Response({})
