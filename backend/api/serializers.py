from rest_framework.serializers import ModelSerializer
from .models import *


class UniversitySerializer(ModelSerializer):
    class Meta:
        model = University
        fields = ['name', 'title', 'id', 'email', 'contact_data', 'description', 'special', 'document']

