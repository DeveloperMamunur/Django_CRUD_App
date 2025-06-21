from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'date_of_admission': forms.DateInput(attrs={'type': 'date'}),
            'gender': forms.RadioSelect(
                choices=(
                    ('male', 'Male'),
                    ('female', 'Female')
                )
            ),
        }

        labels = {
            'name': 'Name',
            'email': 'Email',
            'phone': 'Phone',
            'address': 'Address',
            'gender': 'Gender',
            'date_of_birth': 'Date of Birth',
            'date_of_admission': 'Date of Admission',
            'photo': 'Photo',
            'course': 'Course',
        }

        
