from django.contrib import admin
from .models import Attendance
from .models import Session

admin.site.register(Attendance)
admin.site.register(Session)
