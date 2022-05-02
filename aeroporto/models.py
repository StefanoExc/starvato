from email.policy import default
from django.db import models
from django.forms import IntegerField
from django.contrib.auth.models import User, Group

# Create your models here.

class Aeroporto(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=200)
    continent = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    gps_code = models.CharField(max_length=200)
    iata_code = models.CharField(max_length=3)

    def __str__(self):
        return self.nome

class Aeromobile(models.Model):
    id = models.IntegerField(primary_key=True)
    codice = models.CharField(max_length=200)
    modello = models.CharField(max_length=200)
    percorrenza = models.IntegerField()
    stato = models.BooleanField()
    ultima_manutenzione = models.DateField()
    km_percorsi = models.IntegerField()
    personale_pilota = models.IntegerField()
    personale_assistenza = models.IntegerField()

    def __str__(self):
        return self.codice

class Volo(models.Model):
    id = models.IntegerField(primary_key=True)
    aeroporto_partenza = models.CharField(max_length=200)
    aeroporto_arrivo = models.CharField(max_length=200)
    data_partenza = models.DateField(blank=True,null=True)
    data_arrivo = models.DateField(blank=True,null=True)
    orario_partenza = models.TimeField(blank=True,null=True)
    orario_arrivo = models.TimeField(blank=True,null=True)
    durata_volo = models.FloatField(default=0)
    partenza = models.ForeignKey(Aeroporto,on_delete=models.SET_NULL,null=True,related_name='aeroporto_di_partenza')
    arrivo = models.ForeignKey(Aeroporto, on_delete=models.SET_NULL,null=True,related_name='aeroporto_di_arrivo')
    aereo = models.ForeignKey(Aeromobile, on_delete=models.SET_NULL,null=True)
    posti = models.IntegerField()
    posti_disponibili = models.IntegerField(null=True)
    posti_prenotati = models.IntegerField(null=True)
    codice_volo = models.CharField(max_length=200)
    personale_volo = models.IntegerField()
    personale_assistenza = models.IntegerField()
    sola_andata = models.BooleanField(default=False)
    andata_ritorno = models.BooleanField(default=False)

    def __str__(self):
        return self.codice_volo


class Personale(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=200)
    cognome = models.CharField(max_length=200)
    mansione = models.CharField(max_length=200)
    codice_personale = models.CharField(max_length=200)

    def __str__(self):
        return self.mansione

class Prenotazione(models.Model):
    volo_corrispondente = models.ForeignKey(Volo,on_delete=models.SET_NULL, null=True)
    posto_selezionato = models.CharField(max_length=5, default='')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.id)

    