from django.shortcuts import render
from rest_framework import generics

from api.serializers import BookSerializer
from book.models import Book


# Create your views here.


class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
