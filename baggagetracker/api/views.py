from django.shortcuts import render
from rest_framework import generics

#Import serializers
from .serializers import UsrSerializer

#Import models
from .models import Usr

# Create your views here.

#Return all users
class UsrView(generics.CreateAPIView):
    queryset = Usr.objects.all()
    serializer_class = UsrSerializer

