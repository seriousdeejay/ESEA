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
        if currentuser is not None:
            return CustomUser.objects.filter(id=self.request.user.id)
        if network is not None:
            return CustomUser.objects.filter(accessible_organisations__network=network).distinct() # Should pass organisation id(s) in order to serve the participants of said organisation(s)
        if organisation is not None:
            print(organisation)
            return CustomUser.objects.filter(accessible_organisations=organisation)
        return CustomUser.objects.all()
        
# May be removed if there are no errors
# from django.shortcuts import render
# from rest_framework.response import Response
# from rest_framework.generics import CreateAPIView, RetrieveAPIView
# from .serializers import PostSerializer, RegisterUserSerializer
# from .models import Post
# from rest_framework.permissions import IsAuthenticated

# # Create your views here.

# class PostView(RetrieveAPIView):
#     permission_classes = (IsAuthenticated,) # Authentication needed
#     queryset = Post.objects.all()

#     def get(self, request, *args, **kwargs):
#         queryset = self.get_queryset()
#         serializer = PostSerializer(queryset, many=True)
#         return Response(serializer.data)

# class RegisterUserView(CreateAPIView):
#     serializer_class = RegisterUserSerializer