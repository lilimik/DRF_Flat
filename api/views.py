from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from posts.models import Post, Comment
from posts.serializers import PostCommentsSerializer, CommentCreateSerializer


class PostViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):

    def get_serializer_class(self):
        return PostCommentsSerializer

    def get_queryset(self):
        return Post.objects.all()

    @action(detail=True, methods=['GET'])
    def comments(self, request):
        post = self.get_object()
        serializer = self.get_serializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CommentViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):

    def get_serializer_class(self):
        return CommentCreateSerializer

    def get_queryset(self):
        return Comment.objects.all()
