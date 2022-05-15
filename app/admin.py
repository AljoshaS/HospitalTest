from django.contrib import admin
from .models import Doktori, Pacienti, Oddeli, Pregledi, Hospitalizacija, Upat
# Register your models here.
class DoktoriAdmin(admin.ModelAdmin):

    list_display=('ime','prezime','oddelenie','rakovoditel','telefon')
    list_filter=('specijalizacija','rakovoditel','titula','godini_iskustvo')
    search_fields=('name','prezime','specijalizacija','titula','godini_iskustvo','oddelenie')

class PacientiAdmin(admin.ModelAdmin):

    list_display=('ime','prezime','telefon','pol')
    list_filter=('krvodaritel','pol','osiguran','hronichni_bolesti','alergii')
    search_fields=('ime','prezime','pol')

class OddeliAdmin(admin.ModelAdmin):

    list_display=('ime','kapacitet','broj_pomoshen_personal')
    list_filter=('ime',)
    search_fields=('ime','kapacitet')

class HospitalizacijaAdmin(admin.ModelAdmin):

    @admin.display(description='Ime na pacient')
    def ime_na_pacient(self, obj):
        return obj.pacient.ime

    list_display=('ime_na_pacient','pacient','oddel','broj_soba','broj_krevet','momentalno_hospitaliziran')
    list_filter=('pacient', 'oddel','broj_soba','broj_krevet','momentalno_hospitaliziran')
    search_fields=('pacient','oddel','dijagnoza')

class UpatAdmin(admin.ModelAdmin):

    list_display=('pacient','doktor','oddelenie','termin','prioritet')
    list_filter=('prioritet','termin')
    search_fileds=('doktor','pacient')

class PreglediAdmin(admin.ModelAdmin):

    list_display=('pacient','doktor','oddelenie','datum_pregled','termin')
    list_filter=('datum_pregled','termin','doktor')
    search_fields=('doktor','oddelenie')

admin.site.register(Doktori, DoktoriAdmin)
admin.site.register(Pacienti, PacientiAdmin)
admin.site.register(Oddeli, OddeliAdmin)
admin.site.register(Hospitalizacija, HospitalizacijaAdmin)
admin.site.register(Pregledi, PreglediAdmin)
admin.site.register(Upat, UpatAdmin)
