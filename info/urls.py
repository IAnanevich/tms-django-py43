from django.urls import path

from info import views

urlpatterns = [
    path('', views.read_post, name='read_post')
]
