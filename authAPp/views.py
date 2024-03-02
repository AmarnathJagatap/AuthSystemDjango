# views.py
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from django.conf import settings
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from .models import RevokedToken
from rest_framework.parsers import JSONParser

class LoginAPIView(APIView):
    def post(self, request):
        try:
            email = request.data.get("email")
            password = request.data.get("password")

            user = User.objects.get(email=email)
            if not user.check_password(password):
                return Response(
                    {"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED
                )

            refresh = RefreshToken.for_user(user)

            # Simply get the refresh token as a string
            refresh_token = str(refresh)

            # Store the refresh token in the database (RevokedToken model)
            try:
                RevokedToken.objects.create(token=refresh_token)
            except IntegrityError:
                pass  # Token is already in the database, ignore

            access_token = str(refresh.access_token)

            return Response({"message": "Login Successful", "refresh_token": refresh_token, "access_token": access_token})

        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({"error": f"An error occurred: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class RegistrationAPIView(APIView):
    def post(self, request):
        email = request.data.get("email")
        name = request.data.get("name")
        password = request.data.get("password")

        if User.objects.filter(email=email).exists():
            return Response(
                {"error": "Email already registered"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        user = User.objects.create_user(username=email, email=email, password=password)
        user.first_name = name
        user.save()

        return Response({"Message": "Registered Successfully", "email": email, "user_name": name})

class TestTokenValidityAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = self.request.user
        return Response({"message": f"Token is valid for user {user.username}"})

class RefreshTokenAPIView(APIView):
    def post(self, request):
        refresh_token = request.data.get("refresh_token")

        try:
            revoked_token = RevokedToken.objects.get(token=refresh_token)
            if revoked_token.is_explicit:
                return Response({"error": "Revoked refresh token"}, status=status.HTTP_401_UNAUTHORIZED)
        except ObjectDoesNotExist:
            pass

        try:
            refresh = RefreshToken(refresh_token)
            refresh.verify()
        except Exception as e:
            return Response({"error": f"Invalid refresh token. Reason: {str(e)}"}, status=status.HTTP_401_UNAUTHORIZED)

        # Generate a new access token
        access_token = str(refresh.access_token)

        return Response({"access_token": access_token})

   
    
class LogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        refresh_token = request.data.get("refresh_token")

        try:
            revoked_token = RevokedToken.objects.get(token=refresh_token)
            revoked_token.is_explicit = True
            revoked_token.save()
        except RevokedToken.DoesNotExist:
            pass

        return Response({"message": "Logout Successful"})
