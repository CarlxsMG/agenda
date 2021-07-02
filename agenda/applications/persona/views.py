from django.shortcuts import render
from django.views.generic import (
    ListView,
    TemplateView
)

# Django Rest Framework
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView, # (DETAIL VIEW)
    DestroyAPIView, # (DELETE VIEW)
)

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


class PersonListVien(TemplateView):
    template_name = 'persona/lista.html'
    

class PersonSearchApiView(ListAPIView):
    serializer_class = PersonSerializer

    def get_queryset(self):
        #Filtramos por parametro
        kword = self.kwargs['kword']

        return Person.objects.filter(
            full_name__icontains=kword,
        )
    

class PersonCreateApiView(CreateAPIView):
    serializer_class = PersonSerializer


class PersonDetailApiView(RetrieveAPIView):
    serializer_class = PersonSerializer

    queryset = Person.objects.all()

class PersonDeleteApiView(DestroyAPIView):
    serializer_class = PersonSerializer

    queryset = Person.objects.all()