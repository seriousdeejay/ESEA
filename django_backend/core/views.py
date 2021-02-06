from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework import generics
from .serializers import PostSerializer, RegisterUserSerializer
from .models import Post
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.forms import UserCreationForm

# Create your views here.

class PostView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,) # Authentication needed
    queryset = Post.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)

class RegisterUserView(CreateAPIView):
    serializer_class = RegisterUserSerializer