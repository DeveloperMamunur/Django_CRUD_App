from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm
from django.contrib import messages


# Create your views here.
def student_index(request):
    students = Student.objects.all()
    return render(request, 'student/index.html', {'students': students})

def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Student created successfully")
            return redirect('student_index')
    else:
        form = StudentForm()
    return render(request, 'student/create.html', {'form': form})

def student_edit(request, student_id):
    student = Student.objects.get(id=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Student updated successfully")
            return redirect('student_index')
    else:
        form = StudentForm(instance=student)
    return render(request, 'student/edit.html', {'form': form, 'student': student})