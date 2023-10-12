from django.urls import path

from info import views

urlpatterns = [
    path('test/', views.read_post, name='test'),
    path('posts/', views.PostListView.as_view(), name='post-list'),
    path('posts/<int:pk>', views.PostDetailView.as_view(), name='post-detail'),

]



