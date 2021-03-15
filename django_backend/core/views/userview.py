from rest_framework import viewsets
from rest_framework.generics import CreateAPIView

from ..serializers import RegisterUserSerializer, UserSerializer
from ..models import CustomUser


class RegisterUserView(CreateAPIView):
    serializer_class = RegisterUserSerializer

class UsersViewSet(viewsets.ReadOnlyModelViewSet):
    model = CustomUser
    serializer_class = UserSerializer

    def get_queryset(self):
        currentuser = self.request.GET.get('currentuser', None)
        network = self.request.GET.get('network', None)
        organisation = self.request.GET.get('organisation', None)
        excludeorganisation = self.request.GET.get('excludeorganisation', None)
        if currentuser is not None:
            return CustomUser.objects.filter(id=self.request.user.id)
        if network is not None:
            return CustomUser.objects.filter(organisations__networks=network).distinct() # Should pass network id(s) in order to serve the participants of network(s)
        if organisation is not None:
            return CustomUser.objects.filter(organisations=organisation)
        if excludeorganisation is not None:
            return CustomUser.objects.exclude(organisations=excludeorganisation)
        return CustomUser.objects.all()
