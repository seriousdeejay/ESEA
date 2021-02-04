from django.shortcuts import render
from rest_framework.response import Response
from .serializers import PostSerializer
from .models import Post

# Create your views here.

class PostView(generics.RetrieveAPIView):
    queryset = Posts.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = PostSerializer(queryset, manu=True)
        return Response(serializer.data)
