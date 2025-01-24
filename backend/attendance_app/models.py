from django.db import models
from student_app.models import Student
from course_app.models import Course

class Session(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    duration = models.DurationField()
    date = models.DateField()

    def __str__(self):
        return f"{self.course.name} - {self.date}"

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.student.name} - {self.session.course.name} ({self.session.date})"
