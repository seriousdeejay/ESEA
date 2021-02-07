from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from ..models import Organisation
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

