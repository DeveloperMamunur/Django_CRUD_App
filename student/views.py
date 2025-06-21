from django.shortcuts import render
from .models import Student

# Create your views here.
def student_index(request):
    
    return render(request, 'student/index.html')


