from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import Message
from rest_framework import serializers
from django.contrib.auth.models import User

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password']
        extra_kwargs = {'password': {'write_only': True}}
        
    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    

class MessageSerializer(serializers.ModelSerializer):
    username  = serializers.SerializerMethodField()
    class Meta:
        model = Message
        fields = "__all__"
    
    def get_username(self,obj):
        return obj.user.username if obj.user else None

    