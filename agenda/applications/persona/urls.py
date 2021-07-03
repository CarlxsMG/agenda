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
    path('api/persona/detail/<pk>', views.PersonDetailApiView.as_view(), name='detail'),
    path('api/persona/delete/<pk>', views.PersonDeleteApiView.as_view(), name='delete'),
    path('api/persona/update/<pk>', views.PersonUpdateApiView.as_view(), name='update'),
    path('api/persona/modify/<pk>', views.PersonRetrieveUpdateApiView.as_view(), name='modify'),
    path('api/personas/', views.PersonApiLista.as_view(), name='api-personas'),
    path('api/reuniones/', views.ReunionApiLista.as_view(), name='api-reuniones'),
    path('api/reuniones2/', views.ReunionApiListaLink.as_view(), name='api-reuniones2'),
    path('api/persona/paginacion/', views.PersonPaginationList.as_view(), name='api-paginacion'),  
    path('api/reunion/job/', views.ReunionByPersonJob.as_view(), name='api-reunion-job'),     
]
