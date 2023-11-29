from django.utils.decorators import method_decorator
from django_filters import rest_framework as django_filters
from rest_framework import status, viewsets, filters
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from rest.filters import BookFilter, AuthorFilter
from rest.middleware import BeforeRequestMiddleware, AfterRequestMiddleware
from rest.models import Book, Author
from rest.pagination import BookPagination
from rest.serializers import (
    BookListSerializer,
    BookRetrieveSerializer,
    BookCreateSerializer,
    BookUpdateSerializer,
    BookRecentBooksSerializer,
    BookImageUpdateSerializer,
    AuthorsSerializer,
)
from rest.services import BookService


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.filter(is_deleted=False)
    serializer_class = BookListSerializer
    filter_backends = (django_filters.DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    filterset_class = BookFilter
    ordering_fields = ('id', 'name', 'year', 'author')
    ordering = ('-id', )
    search_fields = ('name', 'year', 'author__last_name', 'author__first_name')
    pagination_class = BookPagination
    permission_classes = (IsAuthenticated, )
    serializer_classes = {
        'list': BookListSerializer,
        'create': BookCreateSerializer,
        'retrieve': BookRetrieveSerializer,
        'update': BookUpdateSerializer,
        'recent_books': BookRecentBooksSerializer,
        'update_image': BookImageUpdateSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.serializer_class)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            print('fnwsncnwsfncwsnefnwecmwpmfvpcmndwpcmnpwepfnwpnmcv')

            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

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

    @action(detail=True, methods=['patch'], url_path='update-image')
    def update_image(self, request, pk=None):
        book = self.get_object()
        serializer = self.serializer_classes.get(self.action, self.serializer_class)(book, request.data, partial=True)

        BookService.update_image(serializer=serializer, instance=book, request=request)

        self.perform_update(serializer)

        return Response(serializer.data)


@method_decorator(BeforeRequestMiddleware, name='dispatch')
@method_decorator(AfterRequestMiddleware, name='dispatch')
class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorsSerializer
    filter_backends = (django_filters.DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    filterset_class = AuthorFilter

    @action(detail=True, methods=['get'], url_path='books')
    def books(self, request, pk=None):
        author = self.get_object()
        books = author.books.all()
        serializer = BookListSerializer(books, many=True)
        return Response(serializer.data)

