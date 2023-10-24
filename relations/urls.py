from django.urls import path

from relations import views

urlpatterns = [
    path('students/', views.StudentsListView.as_view(), name='students'),
    path('students/create/', views.StudentsCreateView.as_view(), name='students-create'),
]
