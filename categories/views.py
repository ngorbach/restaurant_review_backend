from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView

from categories.models import Category
from categories.serializer import CategorySerializer


class ListCategoryView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
