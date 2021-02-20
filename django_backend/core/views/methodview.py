from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from ..models import Method
from ..serializers import MethodSerializer

class MethodViewSet(viewsets.ModelViewSet):
    serializer_class = MethodSerializer

    def get_queryset(self):
        #if False: #self.request.user.is_authenticated:
        #    pass
            # user = self.request.user
            # return Method.objects.filter(Q(organisation that are accessible for user) | Q(ispublic = True)) ??
            # return Organisation.objects.filter(Q(creator=user) | Q(ispublic = True))
        return Method.objects.all()