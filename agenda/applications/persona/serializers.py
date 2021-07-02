# Django Rest Framework
from rest_framework import serializers

# Local models
from .models import Person


class PersonSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Person
        fields = (
            'id',
            'full_name',
            'job',
            'email',
        )