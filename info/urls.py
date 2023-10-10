from django.urls import path

from info import views

urlpatterns = [
    path('test/', views.read_post, name='test'),
    path('posts/', views.PostsView.as_view(), name='posts'),
    path('posts/<int:id>', views.PostsView.as_view(), name='post')

]
