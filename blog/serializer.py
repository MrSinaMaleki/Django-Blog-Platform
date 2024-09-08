from rest_framework import serializers
from blog.models import Post, Author


class PostSerializer(serializers.ModelSerializer):
    # TO Do : What are these ?!
    author_name = serializers.SerializerMethodField()
    author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all())

    class Meta:
        model = Post
        fields = ['id','title', 'description', 'author', 'author_name', 'created_at', 'updated_at']

    def get_author_name(self, obj):
        return obj.author.name  # Adjust based on the field you need




class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'bio', 'email', 'created_at']
