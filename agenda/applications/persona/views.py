from django.shortcuts import render
from django.views.generic import (
    ListView
)

# Django Rest Framework
from rest_framework.generics import ListAPIView

# Local Models
from .models import Person

# Local serializers
from .serializers import PersonSerializer


class ListaPersonas(ListView):
    template_name = 'persona/personas.html'
    context_object_name = 'personas'

    def get_queryset(self):
        return Person.objects.all()


class PersonListApiViwe(ListAPIView):

    serializer_class = PersonSerializer

    def get_queryset(self):
        return Person.objects.all()
    