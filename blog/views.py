from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from blog.models import Post
from blog.serializer import PostSerializer

# Create your views here.


def home(request):
    return render(request, "blog/home.html",{})

@api_view(['GET'])
def all_posts(request):
    serializer = PostSerializer(Post.objects.all(), many=True)
    return Response(serializer.data)

@api_view(['GET'])
def all_authors(request):
    serializer = PostSerializer(Post.objects.all(), many=True)
    return Response(serializer.data)

@api_view(['GET'])
def one_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    serializer = PostSerializer(post)
    return Response(serializer.data)



@api_view(['POST'])
def add_new_post(request):
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




