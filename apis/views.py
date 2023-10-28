'''from rest_framework import generics

from book import Book
from .serializers import BookSerializer


class BookAPIView(generics.BookAPIView):
	queryset = Book.objects.all()
	serializer_class = BookSerializer
'''
from rest_framework import generics
from book.models import Book
from .serializers import BookSerializer

class BookAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer