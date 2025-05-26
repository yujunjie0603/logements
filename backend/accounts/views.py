from django.shortcuts import render
from rest_framework import generics, permissions
from django.contrib.auth.models import User
from .models import CustomUser
from rest_framework.views import APIView
from accounts.serializers import RegisterSerializer, UpdateUserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response

# Create your views here.
class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = (permissions.AllowAny, )
    serializer_class = RegisterSerializer
    
class UpdateUserView(generics.UpdateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UpdateUserSerializer
    
    def get_object(self):
        return self.request.user
    
class LogoutView(APIView):
    
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request):
        
        try:
            refresh_token = request.data['refresh']
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"detail": "Logout and stop old jwt"})
        
        except Exception as e:
            
            return Response({"error": str(e)}, status=400)
            