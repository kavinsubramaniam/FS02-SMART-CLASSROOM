from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_num = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    year = models.IntegerField()
    dept = models.CharField(max_length=100)

    def __str__(self):
        return self.name
