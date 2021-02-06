from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from ..models import Post
from ..serializers import PostSerializer


class PostView(RetrieveAPIView):
    permission_classes = (IsAuthenticated,) # Authentication required
    queryset = Post.objects.all()
    
    def get (self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)