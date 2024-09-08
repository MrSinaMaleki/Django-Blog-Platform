from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from blog.models import Post, Author
from blog.serializer import PostSerializer, AuthorSerializer

# Create your views here.


def home(request):
    return render(request, "blog/home.html",{})

@api_view(['GET'])
def all_posts(request):
    serializer = PostSerializer(Post.objects.all(), many=True)
    return Response(serializer.data)

@api_view(['GET'])
def all_authors(request):
    serializer = AuthorSerializer(Author.objects.all(), many=True)
    return Response(serializer.data)

@api_view(['GET'])
def one_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    serializer = PostSerializer(post)
    return Response(serializer.data)



@api_view(['POST'])
def add_new_post(request):
    # Convert author to integer
    # if 'author' in request.data:
    #     try:
    #         request.data._mutable = True  # Make QueryDict mutable
    #         request.data['author'] = int(request.data['author'])
    #     except ValueError:
    #         return Response({'error': 'Invalid author ID'}, status=status.HTTP_400_BAD_REQUEST)

    serializer = PostSerializer(data=request.data)
    print(request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    print(serializer.errors)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




