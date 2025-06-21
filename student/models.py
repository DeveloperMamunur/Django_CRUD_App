from django.db import models
import os

# Create your models here.
def student_directory_path(instance, filename):
    return os.path.join('student/media/', instance.name, filename)
class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    gender = models.CharField(max_length=10)
    date_of_birth = models.DateField()
    date_of_admission = models.DateField()
    photo = models.ImageField(upload_to=student_directory_path, null=True, blank=True)
    course = models.ForeignKey('course.Course', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
