from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from .serializers import PostSerializer
from .models import Post

# Create your views here.

class PostView(generics.RetrieveAPIView):
    queryset = Post.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)
