from rest_framework.generics import CreateAPIView
from ..serializers import RegisterUserSerializer


class RegisterUserView(CreateAPIView):
    serializer_class = RegisterUserSerializer


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