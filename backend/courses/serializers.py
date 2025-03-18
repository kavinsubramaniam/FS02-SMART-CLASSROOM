from rest_framework import serializers
from .models import Course , Sessions

# Serializer for creating a new course
class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ['teacher', 'name', 'description','resources']
    

    # Create a new user with encrypted password
    # def create(self, validated_data):

    #     course = Course.objects.create(
    #         **validated_data
    #     )
        
    #     return course


class SessionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sessions
        fields = ['course','date','time','duration','topic']