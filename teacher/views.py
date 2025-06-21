from django.shortcuts import render
from .forms import TeacherForm
from django.contrib import messages 
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
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


class teacher_edit(UpdateView):
    form_class = TeacherForm
    model = Teacher
    template_name = 'teacher/edit.html'
    success_url = reverse_lazy('teacher_index')
    pk_url_kwarg = 'teacher_id'

    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, "Teacher updated successfully")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['edit'] = True
        return context


class teacher_delete(DeleteView):
    model = Teacher
    template_name = 'teacher/delete.html'
    success_url = reverse_lazy('teacher_index')
    pk_url_kwarg = 'teacher_id'

    def delete(self, request, *args, **kwargs):
        messages.add_message(self.request, messages.ERROR, "Teacher deleted successfully")
        return super().delete(request, *args, **kwargs)