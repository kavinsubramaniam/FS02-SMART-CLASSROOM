from django.db import models
from admin_app.models import Admin

class Class(models.Model):
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
    dept = models.CharField(max_length=100)
    year = models.IntegerField()

    def __str__(self):
        return f"{self.dept} - {self.year}"
