from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.models import User
from .models import CustomUser


class RegisterSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(write_only=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True)
    email = serializers.EmailField(required=True)
    
    class Meta:
        
        model = CustomUser
        fields = ['username', 'email', 'password', 'password2']
        
    def validate(self, attrs):
        
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError("Les mot de pass ne sont pas identique")
        
        return attrs
    
    def create(self, validated_data):
        
        validated_data.pop('password2')
        user = CustomUser.objects.create_user(**validated_data)
        return user
    
class UpdateUserSerializer(serializers.ManyRelatedField):
    class Meta:
        model = CustomUser
        fields = ['username', 'email']