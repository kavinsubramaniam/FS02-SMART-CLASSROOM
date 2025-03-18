from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegisterSerializer

# Registration view using DRF's generics.CreateAPIView
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

# Login view using APIView for custom behavior
class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        # Authenticate the user using Django's built-in authenticate method
        user = authenticate(username=username, password=password)
        if user is not None:
            # Generate JWT tokens using simplejwt's RefreshToken
            refresh = RefreshToken.for_user(user)
            return Response({
                "refresh": str(refresh),
                "access": str(refresh.access_token)
            })
        else:
            return Response({"error": "Invalid Credentials"},
                            status=status.HTTP_401_UNAUTHORIZED)
