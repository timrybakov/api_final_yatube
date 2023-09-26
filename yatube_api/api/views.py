from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from posts.models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from .permissions import UserPostPatchPutDeletePermission


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (UserPostPatchPutDeletePermission,)

    def get_permissions(self):
        if self.action in ('retrieve', 'list'):
            return (IsAuthenticatedOrReadOnly(),)
        return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            post=self.kwargs.get('post_id')
        )
