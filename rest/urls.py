from django.urls import path
from rest_framework.routers import DefaultRouter

from rest import views

app_name = 'books'

# urlpatterns = [
#     path('books/', views.BookListCreateView.as_view(), name='books'),
#     path('books/<int:pk>', views.BookRetrieveUpdateDeleteView.as_view(), name='books-update'),
# path('books/', views.BookView.as_view(), name='books'),
# path('books/<int:pk>', views.SingleBookView.as_view(), name='book'),
# path('books/', views.BookViewSet.as_view({'get': 'list'}), name='books'),
# path('books/<int:pk>', views.BookViewSet.as_view({'get': 'retrieve'}), name='book'),
# ]

router = DefaultRouter()
router.register(r'books', views.BookViewSet, basename='books')
router.register(r'authors', views.AuthorViewSet, basename='authors')


# urlpatterns += router.urls
urlpatterns = router.urls
