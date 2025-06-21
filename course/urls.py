from django.urls import path
from . import views

urlpatterns = [
    path('course/', views.course_index, name='course_index'),
    path('course/create/', views.course_create, name='course_create'),
    path('course/edit/<int:course_id>/', views.course_edit, name='course_edit'),
    path('course/delete/<int:course_id>/', views.course_delete, name='course_delete'),
]