from django.db import models
from teacher_app.models import Teacher
from class_app.models import Class

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    creator = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    classes = models.ManyToManyField(Class)

    def __str__(self):
        return self.name
