from functools import partial
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from .serializers import ProductListSerializer
from .models import Product

# Create your views here.
class ProductViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Product.objects.all()
        serializer = ProductListSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, id=None):
        queryset = Product.objects.all()
        product = get_object_or_404(queryset, id=id)
        serializer = ProductListSerializer(product)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = ProductListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, id, format=None):
        queryset = Product.objects.all()
        product = get_object_or_404(queryset, id=id)
        serializer = ProductListSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self, request, id, format=None):
        queryset = Product.objects.all()
        product = get_object_or_404(queryset, id=id)
        serializer = ProductListSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update']:
            permission_classes = [permissions.IsAdminUser]
        else:
            permission_classes = [permissions.AllowAny]
        
        return [permission() for permission in permission_classes]
    