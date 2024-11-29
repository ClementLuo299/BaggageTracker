from django.shortcuts import render
from rest_framework import generics
from .serializers import UsrSerializer
from .models import Usr

# Create your views here.

#Return all users
class UsrView(generics.ListAPIView):
    queryset = Usr.objects.all()
    serializer_class = UsrSerializer

