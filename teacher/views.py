from django.shortcuts import render
from .forms import TeacherForm
from django.contrib import messages 
from django.views.generic import CreateView, ListView
from .models import Teacher
from django.urls import reverse_lazy

# Create your views here.
class teacher_index(ListView):
    model = Teacher
    template_name = 'teacher/index.html'
    context_object_name = 'teachers'
    


class teacher_create(CreateView):
    form_class = TeacherForm
    template_name = 'teacher/create.html'
    success_url = reverse_lazy('teacher_index')

    def from_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, "Teacher created successfully")
        return super().form_valid(form)


