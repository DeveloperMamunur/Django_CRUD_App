from django.shortcuts import render, redirect
from .models import Course
from django.contrib import messages
# Create your views here.
def course_index(request):
    courses = Course.objects.all()
    return render(request, 'course/index.html', {'courses': courses})

def course_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        course_code = request.POST.get('course_code')
        credit = request.POST.get('credit')
        price = request.POST.get('price')

        course = Course(name=name, course_code=course_code, credit=credit, price=price)
        course.save()
        messages.add_message(request, messages.SUCCESS, "Course created successfully")
        return redirect('course_index')

    return render(request, 'course/create.html')

def course_edit(request, course_id):
    course = Course.objects.get(id=course_id)
    if request.method == 'POST':
        name = request.POST.get('name')
        course_code = request.POST.get('course_code')
        credit = request.POST.get('credit')
        price = request.POST.get('price')

        course = Course(name=name, course_code=course_code, credit=credit, price=price)
        course.save()
        messages.add_message(request, messages.INFO, "Course updated successfully")
        return redirect('course_index')

    return render(request, 'course/edit.html', {'course': course})