from django.shortcuts import render
from .serializers import CourseSerializer , SessionSerializer
from rest_framework import generics
from .models import Course , Sessions

__all__ = [
    'CreateCourseView', 'ListCourseView', 'UpdateCourseView', 'DeleteCourseView',
    'CreateSessionView', 'ListSessionView', 'SessionDetailView',    ]

class CreateCourseView(generics.CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class ListCourseView(generics.ListAPIView):
   
    serializer_class = CourseSerializer

    def get_queryset(self):
        return Course.objects.all()
    
class UpdateCourseView(generics.UpdateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class DeleteCourseView(generics.DestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CreateSessionView(generics.CreateAPIView):
    queryset = Sessions.objects.all()
    serializer_class = SessionSerializer

class ListSessionView(generics.ListAPIView):
   
    serializer_class = SessionSerializer

    def get_queryset(self):
        course_id = self.kwargs['course_id']
        return Sessions.objects.filter(course=course_id)
    
class SessionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sessions.objects.all()
    serializer_class = SessionSerializer