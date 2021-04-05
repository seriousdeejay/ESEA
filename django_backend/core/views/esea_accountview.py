from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from ..models import EseaAccount
from ..serializers import EseaAccountSerializer

class EseaAccountViewSet(viewsets.ModelViewSet):
    serializer_class = EseaAccountSerializer

    def get_queryset(self):
        organisation = self.request.GET.get('organisation', None)
        if organisation is not None:
            return EseaAccount.objects.filter(organisation=organisation)
        return EseaAccount.objects.filter(campaign = self.kwargs['campaign_pk'])

    def update(self, request, network_pk, campaign_pk, pk):
        esea_account = get_object_or_404(EseaAccount, pk=pk)
        serializer = EseaAccountSerializer(esea_account, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        print(esea_account.sufficient_response_rate()) # Maybe i have to put this in the serializer update method? If sufficient_response_rate gets returned a report can be created
        return Response(serializer.data)
