from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=100)
    course_code = models.CharField(max_length=10)
    credit = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # duration = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
