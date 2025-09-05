from django.shortcuts import render
from olcha.models import Category, Product
from olcha.serializers import CategorySerializer, ProductSerializers, ProductDetailSerializer
from rest_framework import permissions
from rest_framework.generics import ListAPIView, RetrieveAPIView

# Create your views here.

class CategoryListAPIView(ListAPIView):
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Category.objects.filter(parent__isnull=True)
        return queryset
    

class SubcategoryListAPIView(ListAPIView):
    serializer_class = CategorySerializer


    def get_queryset(self):
        parent_slug =self.kwargs['parent_slug']
        parent_category = Category.objects.get(slug=parent_slug)
        return parent_category.children.all()




class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers


class ProductDetailAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    lookup_field = "id"   


