from rest_framework import status, generics, mixins, viewsets
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from rest.models import Book, Author
from rest.serializers import BookListSerializer, AuthorsSerializer, BookRetrieveSerializer, \
    BookCreateSerializer, BookUpdateSerializer, BookRecentBooksSerializer


# class BookListCreateView(APIView):
#     def get(self, request):
#         # name = request.query_params.get('name')
#         books = Book.objects.all()
#         serializer = BookSerializer(books, many=True)
#         return Response({'books': serializer.data})
#
#     def post(self, request):
#         books = request.data.get('books')
#
#         serializer = BookSerializer(data=books)
#         if serializer.is_valid(raise_exception=True):
#             new_book = serializer.save()
#         list_serializer = BookSerializer(new_book)
#         return Response({'new_book': list_serializer.data})
#
#
# class BookRetrieveUpdateDeleteView(APIView):
#     def get(self, request, pk):
#         books = Book.objects.get(id=pk)
#         serializer = BookSerializer(books)
#         return Response({'books': serializer.data})
#
#     def put(self, request, pk):
#         book = get_object_or_404(Book.objects.all(), pk=pk)
#         data = request.data.get('books')
#         serializer = BookSerializer(data=data, instance=book, partial=True)
#
#         if serializer.is_valid(raise_exception=True):
#             new_book = serializer.save()
#         list_serializer = BookSerializer(new_book)
#         return Response({'updated_book': list_serializer.data})
#
#     def delete(self, request, pk):
#         book = get_object_or_404(Book.objects.all(), pk=pk)
#         book.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# class BookView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
# class BookView(generics.ListCreateAPIView):
#     queryset = Book.objects.filter(is_deleted=False)
#     serializer_class = BookSerializer
#
#     def list(self, request, *args, **kwargs):
#         year = request.query_params.get('year')
#         sorting = request.query_params.get('sorting')
#         if year:
#             self.queryset = self.queryset.filter(year__gte=year)
#         if sorting:
#             self.queryset = self.queryset.order_by(sorting)
#         return super().list(request, *args, **kwargs)
#
#     # def get(self, request, *args, **kwargs):
#     #     return self.list(request, *args, **kwargs)
#     #
#     # def post(self, request, *args, **kwargs):
#     #     return self.create(request, *args, **kwargs)
#
#
# class SingleBookView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Book.objects.filter(is_deleted=False)
#     serializer_class = SingleBookSerializer
#
#     # def retrieve(self, request, *args, **kwargs):
#     #     print(request.query_params)
#     #     return super().retrieve(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         book = self.get_object()
#         book.is_deleted = True
#         book.save()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# class BookViewSet(viewsets.ViewSet):
#
#     def list(self, request):
#         queryset = Book.objects.all()
#         serializer = BookSerializer(queryset, many=True)
#         return Response(serializer.data)
#
#     def retrieve(self, request, pk=None):
#         queryset = Book.objects.all()
#         book = get_object_or_404(queryset, pk=pk)
#         serializer = SingleBookSerializer(book)
#         return Response(serializer.data)


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.filter(is_deleted=False)
    serializer_class = BookListSerializer
    serializer_classes = {
        'list': BookListSerializer,
        'create': BookCreateSerializer,
        'retrieve': BookRetrieveSerializer,
        'update': BookUpdateSerializer,
        'recent_books': BookRecentBooksSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.serializer_class)

    def destroy(self, request, *args, **kwargs):
        book = self.get_object()
        book.is_deleted = True
        book.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=['get'], url_path='recent-books')
    def recent_books(self, request):
        recent_books = Book.objects.filter(year__gte=2020)
        serializer = self.serializer_classes.get(self.action, self.serializer_class)(recent_books, many=True)
        return Response(serializer.data)


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorsSerializer

    @action(detail=True, methods=['get'], url_path='books')
    def books(self, request, pk=None):
        author = self.get_object()
        books = author.books.all()
        serializer = BookListSerializer(books, many=True)
        return Response(serializer.data)

