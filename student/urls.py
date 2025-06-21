from django.urls import path
from . import views

urlpatterns = [
    path('student/', views.student_index, name='student_index'),
]