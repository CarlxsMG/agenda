from django.shortcuts import render
from django.views.generic import (
    ListView
)

# Local Models
from .models import Person


class ListaPersonas(ListView):
    template_name = 'persona/personas.html'
    context_object_name = 'personas'

    def get_queryset(self):
        return Person.objects.all()


