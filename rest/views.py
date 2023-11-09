from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from rest.models import Book
from rest.serializers import BookSerializer


class BookListCreateView(APIView):
    def get(self, request):
        # name = request.query_params.get('name')
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response({'books': serializer.data})

    def post(self, request):
        books = request.data.get('books')

        serializer = BookSerializer(data=books)
        if serializer.is_valid(raise_exception=True):
            new_book = serializer.save()
        list_serializer = BookSerializer(new_book)
        return Response({'new_book': list_serializer.data})


class BookRetrieveUpdateDeleteView(APIView):
    def get(self, request, pk):
        books = Book.objects.get(id=pk)
        serializer = BookSerializer(books)
        return Response({'books': serializer.data})

    def put(self, request, pk):
        book = get_object_or_404(Book.objects.all(), pk=pk)
        data = request.data.get('books')
        serializer = BookSerializer(data=data, instance=book, partial=True)

        if serializer.is_valid(raise_exception=True):
            new_book = serializer.save()
        list_serializer = BookSerializer(new_book)
        return Response({'updated_book': list_serializer.data})

    def delete(self, request, pk):
        book = get_object_or_404(Book.objects.all(), pk=pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
