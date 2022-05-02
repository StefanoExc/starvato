from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Aeroporto,Aeromobile, Prenotazione,Volo,Personale

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'groups']
        
class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class AeroportoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aeroporto
        fields = ['id','nome','continent','type','gps_code','iata_code']

class AeromobileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aeromobile
        fields = ['id','codice','modello','percorrenza','stato','ultima_manutenzione','km_percorsi','personale_pilota','personale_assistenza']

class VoloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Volo
        fields = ['id','aeroporto_partenza','aeroporto_arrivo','data_partenza','data_arrivo','orario_partenza','orario_arrivo',
        'durata_volo','partenza','arrivo','aereo','posti','posti_disponibili','posti_prenotati','codice_volo','personale_volo',
        'personale_assistenza','sola_andata','andata_ritorno']

class PersonaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personale
        fields = ['id','nome','cognome','mansione','codice_personale']

class PrenotazioneSerializer(serializers.ModelSerializer):
    volo_corrispondente = VoloSerializer()
    class Meta:
        model = Prenotazione
        fields = ['id','user','volo_corrispondente','posto_selezionato']
        
