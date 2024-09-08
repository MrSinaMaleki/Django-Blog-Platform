from rest_framework import serializers
from blog.models import Post,Author


class PostSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all())
    class Meta:
        model = Post
        fields = ['title', 'description', 'author', 'created_at', 'updated_at']


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id','name', 'bio', 'email', 'created_at']
