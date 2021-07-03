# Django Rest Framework
from rest_framework import serializers

# Local models
from .models import Person


class PersonSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Person
        fields = ('__all__')


class PersonaSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    full_name = serializers.CharField()
    job = serializers.CharField()
    email = serializers.EmailField()
    phone = serializers.CharField()

    # Con required, especificas que si el modelo no lo tiene, que lo ignore y no produzca un error
    activo = serializers.BooleanField(required=False)


class PersonaSerializer2(serializers.ModelSerializer):
    
    activo = serializers.BooleanField(required=False, default=False)

    class Meta:
        model = Person
        fields = ('__all__')