from rest_framework import serializers
from posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    slug = serializers.SlugField(read_only=True)
    image = serializers.ImageField(read_only=True)
    class Meta:
        model = Post
        fields = "__all__"

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["image"]