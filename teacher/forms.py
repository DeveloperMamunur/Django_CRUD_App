from django import forms
from . import models

class TeacherForm(forms.ModelForm):
    class Meta:
        model = models.Teacher
        fields = '__all__'

        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'date_of_joining': forms.DateInput(attrs={'type': 'date'}),
            'gender': forms.RadioSelect(
                choices=(
                    ('male', 'Male'),
                    ('female', 'Female'),
                )
            )
        }

        labels = {
            'name': 'Name',
            'email': 'Email',
            'phone': 'Phone',
            'address': 'Address',
            'gender': 'Gender',
            'date_of_birth': 'Date of Birth',
            'date_of_joining': 'Date of Joining',
            'photo': 'Photo',
            'qualification': 'Qualification',
            'subject': 'Subject',
            'salary': 'Salary',
            'course': 'Course',
        }