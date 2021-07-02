# Django imports
from django.urls import path

# Local views
from . import views


app_name = 'persona_app'

urlpatterns = [
    path('personas/', views.ListaPersonas.as_view(), name='personas'),
    path('api-persona-list/', views.PersonListApiViwe.as_view())
]
