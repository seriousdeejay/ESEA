from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from django.db.models import Q

from ..models import Organisation, CustomUser
from ..serializers import OrganisationSerializer


class OrganisationView(generics.ListCreateAPIView): # RetrieveAPIView):
    # permission_classes = (IsAuthenticated,) # Authentication required
    queryset = Organisation.objects.all()
    serializer_class = OrganisationSerializer


class OrganisationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Organisation.objects.all()
    serializer_class = OrganisationSerializer

    # def post(self, request, *args, **kwargs):
    #     print(str(request.POST))

    #     # obj = form.save(commit = False)
    #     # obj.owner = request.user
    #     # print(obj)
    #     return Response()

    # def get(self, request, *args, **kwargs):
    #      queryset = self.get_queryset()
    #      serializer = PostSerializer(queryset, many=True)
    #      return Response(serializer.data)

class OrganisationViewSet(viewsets.ModelViewSet):
    serializer_class = OrganisationSerializer
    queryset = Organisation.objects.all()

class PersonalOrganisationViewSet(viewsets.ModelViewSet):
    serializer_class = OrganisationSerializer
   
    def get_queryset(self):
        if self.request.user.is_authenticated:
            user = self.request.user
            return Organisation.objects.filter(Q(creator=user) | Q(ispublic = True))
        return Organisation.objects.all()