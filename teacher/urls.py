from django.urls import path
from . import views

urlpatterns = [
    path('teacher/', views.teacher_index.as_view(), name='teacher_index'),
    path('teacher/create/', views.teacher_create.as_view(), name='teacher_create'),
    
]