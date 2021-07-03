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
    UpdateAPIView, #(SIN DATOS EN INPUTS)
    RetrieveUpdateAPIView, # (CON DATOS EN INPUTS)
)

# Local Models
from .models import Person, Reunion

# Local serializers
from .serializers import (
    PersonSerializer,
    PersonaSerializer,
    PersonaSerializer2,
    ReunionSerializer,
    PersonaSerializer3,
)


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

class PersonUpdateApiView(UpdateAPIView):
    serializer_class = PersonSerializer

    queryset = Person.objects.all()


class PersonRetrieveUpdateApiView(RetrieveUpdateAPIView):
    serializer_class = PersonSerializer

    queryset = Person.objects.all()


class PersonApiLista(ListAPIView):
    ''' Vista para interactuar con serializadores '''

    # serializer_class = PersonaSerializer
    serializer_class = PersonaSerializer3

    def get_queryset(self):
        return Person.objects.all()
    

class ReunionApiLista(ListAPIView):

    serializer_class = ReunionSerializer

    def get_queryset(self):
        return Reunion.objects.all()