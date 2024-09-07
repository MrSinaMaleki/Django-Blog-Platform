from rest_framework import serializers
from blog.models import Post


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='name', many=True)
    class Meta:
        model = Post
        fields = ['title', 'description', 'author', 'created_at', 'updated_at']
