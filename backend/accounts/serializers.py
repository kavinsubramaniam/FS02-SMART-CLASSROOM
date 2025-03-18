from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from .models import Student, Teacher

# Serializer for registering new users
class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(write_only=True, min_length=6)
    confirm_password = serializers.CharField(write_only=True, min_length=6)

    designation = serializers.ChoiceField(
        choices=['student', 'teacher'] ,
        write_only=True
    ) 

    class Meta:
        model = User
        fields = ['username', 'email', 'password','confirm_password','designation']

    def validate(self, data):
        """
        Check that the two password entries match.
        """
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    # Create a new user with encrypted password
    def create(self, validated_data):

        designation = validated_data.pop('designation')

        validated_data.pop('confirm_password')


        user = User.objects.create_user(
            **validated_data
        )

        if(designation == 'student'):
            Student.objects.create(user=user,email=validated_data['email'])
        else:  
            Teacher.objects.create(user=user,email=validated_data['email'])

        
        return user
