from rest_framework import generics


from .models import Post
from .permissions import IsAuthorOrReadOnly # NEW
from .serializers import PostSerializer


class PostList(generics.ListCreateAPIView):

    # permission_classes = (permissions.IsAuthenticated,) # NEW
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = (IsAuthorOrReadOnly,)  # NEW
    queryset = Post.objects.all()
    serializer_class = PostSerializer
