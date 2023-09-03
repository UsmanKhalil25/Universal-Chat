from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Message
from .serializers import MessageSerializer,UserSerializer
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User

# Create your views here.

@api_view(["POST"])
def registerUser(request):
    if request.method == "POST":
        serializer = UserSerializer(data =request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_200_OK)
        return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)
    

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getMessages(request):
    if request.method == "GET":
        messages = Message.objects.all()
        serializer = MessageSerializer(messages,many = True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def sendMessage(request):
    if request.method == "POST":
        message = request.data
        serializer = MessageSerializer(data = message,many = False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status =status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

