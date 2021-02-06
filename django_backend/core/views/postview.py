from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from ..models import Post
from ..serializers import PostSerializer

class PostView(generics.ListCreateAPIView): # RetrieveAPIView):
    # permission_classes = (IsAuthenticated,) # Authentication required
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

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

