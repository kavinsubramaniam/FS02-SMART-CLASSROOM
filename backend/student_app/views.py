from rest_framework import viewsets
from .serializers import StudentSerializer
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Student
from face_recognition.registration import FaceRegistration

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

def register_faces(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    face_reg = FaceRegistration(student)

    try:
        face_reg.update_student_folder()
        return JsonResponse({"message": "Face registration successful"}, status=200)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
