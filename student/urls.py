from django.urls import path
from . import views

urlpatterns = [
    path('student/', views.student_index, name='student_index'),
    path('student/create/', views.student_create, name='student_create'),
    path('student/edit/<int:student_id>/', views.student_edit, name='student_edit'),
    
]