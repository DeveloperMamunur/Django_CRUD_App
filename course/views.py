from django.shortcuts import render

# Create your views here.
def course_index(request):
    return render(request, 'course/index.html')