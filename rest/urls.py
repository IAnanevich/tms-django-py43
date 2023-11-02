from django.urls import path

from rest import views

app_name = 'books'

urlpatterns = [
    path('books/', views.BookListCreateView.as_view(), name='books'),
    path('books/<int:pk>', views.BookRetrieveUpdateDeleteView.as_view(), name='books-update'),
]
