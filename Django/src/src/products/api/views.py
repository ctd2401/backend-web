from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from products.models import Product
from products.api.serializers import ProductSerializer
@api_view(['GET'])
def api_detail_product_view(request,id):

    try:
        product_post = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = ProductSerializer(product_post)
        return Response(serializer.data)
@api_view(['PUT',])
def api_update_product_view(request,id):

    try:
        product_post = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":
        serializer = ProductSerializer(product_post,data = request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["success"] = "update successful"
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['DELETE',])
def api_delete_product_view(request,id):

    try:
        product_post = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "DELETE":
        operation = product_post.delete()
        data = {}
        if operation:
            data["success"] = "delete successful"
        else:
            data["failure"] = "delete failed"
        return Response(data=data)

