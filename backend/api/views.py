from django.shortcuts import render
from rest_framework import permissions
from rest_framework.generics import ListAPIView
from .models import *
from .serializers import *


class UniversityApiView(ListAPIView):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer
    permission_classes = [permissions.AllowAny]
