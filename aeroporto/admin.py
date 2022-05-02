from django.contrib import admin
from .models import Aeroporto,Personale,Prenotazione,Volo,Aeromobile

# Register your models here.
admin.site.register(Aeroporto)
admin.site.register(Personale)
admin.site.register(Volo)
admin.site.register(Aeromobile)
admin.site.register(Prenotazione)
