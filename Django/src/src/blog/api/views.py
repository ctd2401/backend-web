from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from products.models import Product
from blog.models import Article
from blog.api.serializers import ArticleSerializer
@api_view(['GET'])
def api_detail_blog_view(request,id):

    try:
        blog_post = Article.objects.get(id=id)
    except Article.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = ArticleSerializer(blog_post)
        return Response(serializer.data)
@api_view(['PUT',])
def api_update_blog_view(request,id):

    try:
        blog_post = Article.objects.get(id=id)
    except Article.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":
        serializer = ArticleSerializer(blog_post,data = request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["success"] = "update successful"
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['DELETE',])
def api_delete_blog_view(request,id):

    try:
        blog_post = Article.objects.get(id=id)
    except Article.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "DELETE":
        operation = blog_post.delete()
        data = {}
        if operation:
            data["success"] = "delete successful"
        else:
            data["failure"] = "delete failed"
        return Response(data=data)
