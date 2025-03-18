from django.db import models
from accounts.models import Teacher

class Course(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    resources = models.TextField()

    def __str__(self):
        return self.name
    
class Sessions(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    duration = models.DurationField()
    topic = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.course.name} - {self.topic}"