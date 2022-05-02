from ast import Return
from hashlib import new
from multiprocessing import context
from urllib import response
from django.shortcuts import render
from .models import Aeroporto,Volo,Aeromobile,Personale,Prenotazione
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import AeromobileSerializer, PersonaleSerializer, PrenotazioneSerializer, UserSerializer, GroupSerializer, AeroportoSerializer, VoloSerializer
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from aeroporto import serializers
# Create your views here.

def aeroporto(request):
    aeroporti = Aeroporto.objects.all()
    return render(request,'aeroporto/home.html',{'aeroporto': aeroporti})

def volo(request):
    voli = Volo.objects.all()
    return render(request,'aeroporto/prenotazioni.html',{'volo' : voli})

def aeromobile(request):
    aeromobili = Aeromobile.objects.all()
    partenza=Aeroporto.objects.all()
    arrivo=Aeroporto.objects.all()
    context_data={
        'aeromobile': aeromobili,
        'partenza':partenza,
        'arrivo':arrivo
    }
    return render(request,'aeroporto/posti.html',context_data)

def personale(request):
    personale = Personale.objects.all()
    return render(request,'aeroporto/registrati.html',{'personale': personale})

def prenotazioni(request):
    prenotazioni = Prenotazione.objects.all()
    return render(request, 'aeroporto/mie_prenotazioni.html',{'prenotazioni': prenotazioni})

def contatti(request):
    return render(request,'aeroporto/contatti.html',{})

def attribuisci_prenotazione(request, format=None):
    prenotazione = Prenotazione.objects.all()
    return render(request,'aeroporto/conferma.html',{'prenotazione': prenotazione})

@api_view(['POST'])
@csrf_exempt
def get_biglietti(request,format = None):
    print('ciao')
    print(request.data)
    print(request.data['data1'])
    volo = Volo.objects.filter(aeroporto_partenza = request.data['aeroporto1'],aeroporto_arrivo = request.data['aeroporto2'],
    data_partenza = request.data['data1'],data_arrivo = request.data['data2'])
    serializer = VoloSerializer(volo, many = True, context={'request': request})
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
@csrf_exempt
def acquista_biglietto(request,format = None):
    print(request.data)
    print(request.data['id_volo'])
    biglietto = Volo.objects.get(id = request.data['id_volo'])
    biglietto.posti_disponibili = biglietto.posti_disponibili - int(request.data['viaggiatori'])
    biglietto.posti_prenotati = biglietto.posti_prenotati + int(request.data['viaggiatori'])
    biglietto.save()
    serializer = VoloSerializer(biglietto, context={'request': request})
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST','OPTIONS'])
@csrf_exempt
def addPrenotazione(request):
    volo = Volo.objects.get(id = request.data['id_volo'])
    user = User.objects.get(id = request.data['id_user'])
    for posto in request.data['posti']:
        prenotazione = Prenotazione()
        prenotazione.volo_corrispondente = volo
        prenotazione.posto_selezionato = posto
        prenotazione.user = user
        prenotazione.save()
    queryset = Prenotazione.objects.all().order_by('-id')[:len(request.data['posti'])]
    print(queryset)
    serializer = PrenotazioneSerializer(queryset, context={'request':request})
    return Response(serializer.data, status = status.HTTP_200_OK)

@api_view(['POST'])
@csrf_exempt
def getPostiPrenotati(request,format = None):
    prenotazione = Prenotazione.objects.filter(volo_corrispondente = request.data['volo_corrispondente']).prefetch_related('user', 'volo_corrispondente')
    serializer = PrenotazioneSerializer(prenotazione,many=True, context={'request': request})
    print(serializer.data)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
@csrf_exempt
def getUser(request,format = None):
    prenotazione = Prenotazione.objects.filter(id_user = request.data['id'])
    serializer = PrenotazioneSerializer(prenotazione,many=True, context={'request': request})
    print(serializer.data)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@csrf_exempt
def getUserPrenotazioni(request,format = None):
    user = Prenotazione.objects.filter(user = 1) 
    serializer = PrenotazioneSerializer(user, many = True, context={'request': request})
    return Response(serializer.data, status=status.HTTP_200_OK)
  

def selezione(request):
    return render(request,'aeroporto/posti2.html',{})

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class AeroportoViewSet(viewsets.ModelViewSet):
    queryset = Aeroporto.objects.all().order_by('id')
    serializer_class = AeroportoSerializer

class AeromobileViewSet(viewsets.ModelViewSet):
    queryset = Aeromobile.objects.all().order_by('id')
    serializer_class = AeromobileSerializer

class VoloViewSet(viewsets.ModelViewSet):
    queryset = Volo.objects.all().order_by('id')
    serializer_class = VoloSerializer

class PersonaleViewSet(viewsets.ModelViewSet):
    queryset = Personale.objects.all().order_by('id')
    serializer_class = PersonaleSerializer

class PrenotazioneViewSet(viewsets.ModelViewSet):
    queryset = Prenotazione.objects.all().order_by('user')
    serializer_class = PrenotazioneSerializer

def index(request):
   if request.method == 'POST':
      var = request.POST['aeroporto1','aeroporto2','data1','data2']


