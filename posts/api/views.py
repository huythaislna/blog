from rest_framework.viewsets import ModelViewSet
from posts.api.serializers import PostSerializer, ImageSerializer
from posts.models import Post
from posts.api.permissions import IsUpdated
from django.utils.text import slugify
from rest_framework.generics import UpdateAPIView


class PostViewSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [IsUpdated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)

class ImageUpdateAPIView(UpdateAPIView):
    serializer_class = ImageSerializer
    queryset = Post.objects.all()
    permission_classes = [IsUpdated]
