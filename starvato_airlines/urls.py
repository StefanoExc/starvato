"""starvato_airlines URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from aeroporto import views
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'aeroporti', views.AeroportoViewSet)
router.register(r'aeromobili', views.AeromobileViewSet)
router.register(r'voli', views.VoloViewSet)
router.register(r'dipendenti', views.PersonaleViewSet)
router.register(r'prenotazione', views.PrenotazioneViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('aeroporto/', views.aeroporto, name ='home'),
    path('aeroporto/contatti', views.contatti, name ='contattaci'),   
    path('aeroporto/registrati', views.personale, name = 'registrati'),
    path('aeroporto/posti', views.aeromobile, name = 'prenota'),
    path('aeroporto/posti2',views.selezione, name = 'selezione_volo'),
    path('aeroporto/biglietti',views.get_biglietti, name = 'biglietti'),
    path('aeroporto/prenotazioni', views.volo, name = 'prenotazioni'),
    path('', include(router.urls)),
    path('aeroporto/biglietti/acquista',views.acquista_biglietto, name = 'acquista'),
    path('aeroporto/store',views.addPrenotazione, name = 'store_prenotazione'),
    path('aeroporto/volo', views.getPostiPrenotati, name = 'posti_prenotati'),
    path('aeroporto/conferma', views.attribuisci_prenotazione, name = 'conferma_prenotazione'),
    path('aeroporto/mie_prenotazioni', views.prenotazioni, name = 'mie_prenotazioni'),
    path('aeroporto/user', views.getUserPrenotazioni, name = 'user')
]
