from django.urls import path
from . import views

urlpatterns = [
    path('course/', views.course_index, name='course_index'),
    path('course/create/', views.course_create, name='course_create'),
    
]