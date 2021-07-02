# Django imports
from django.urls import path

# Local views
from . import views


app_name = 'persona_app'

urlpatterns = [
    path('personas/', views.ListaPersonas.as_view(), name='personas'),
    path('api/persona/lista/', views.PersonListApiViwe.as_view()),
    path('lista/', views.PersonListVien.as_view(), name='lista'),
    path('api/persona/search/<kword>/', views.PersonSearchApiView.as_view(), name='search'),
    path('api/persona/create/', views.PersonCreateApiView.as_view(), name='create'),
]
