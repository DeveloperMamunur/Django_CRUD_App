from django.db import models
import os

# Create your models here.
def teacher_directory_path(instance, filename):
    return os.path.join('teacher/media/', instance.name, filename)

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    gender = models.CharField(max_length=10)
    date_of_birth = models.DateField()
    date_of_joining = models.DateField()
    photo = models.ImageField(upload_to=teacher_directory_path, null=True, blank=True)
    qualification = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    course = models.ForeignKey('course.Course', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
