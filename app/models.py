from django.db import models
import random
from datetime import timedelta
from django.utils.timezone import now

# Create your models here.

class Doktori(models.Model):
    ime=models.CharField(max_length=50)
    prezime=models.CharField(max_length=50)
    telefon=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    titula=models.CharField(max_length=50)
    oddelenie=models.CharField(max_length=50)
    specijalizacija=models.CharField(max_length=50)
    faksimil=models.IntegerField(unique=True)
    godini_iskustvo=models.IntegerField()
    plata=models.IntegerField()
    rakovoditel=models.BooleanField()

class Pacienti(models.Model):
    ime=models.CharField(max_length=50)
    prezime=models.CharField(max_length=50)
    telefon=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    data_ragjanje=models.DateField()
    embg=models.CharField(max_length=50, unique=True)
    pol=models.CharField(max_length=50)
    krvodaritel=models.BooleanField()
    krvna_grupa=models.CharField(max_length=50)
    osiguran=models.BooleanField()
    hronichni_bolesti=models.BooleanField()
    hronichni_zabeleshka=models.TextField(null=True, blank=True)
    alergii=models.BooleanField()
    alergii_zabeleshka=models.TextField(null=True, blank=True)

class Oddeli(models.Model):
    ime=models.CharField(max_length=50)
    kapacitet=models.IntegerField()
    broj_pomoshen_personal=models.IntegerField()


class Hospitalizacija(models.Model):
    pacient=models.ForeignKey(Pacienti, on_delete=models.CASCADE, null=True)
    oddel=models.ForeignKey(Oddeli, on_delete=models.CASCADE, null=True)
    data=models.DateField()
    dijagnoza=models.CharField(max_length=50)
    rezultati=models.TextField(null=True, blank=True)
    broj_soba=models.IntegerField()
    broj_krevet=models.IntegerField()
    terapija=models.TextField(null=True, blank=True)
    momentalno_hospitaliziran=models.BooleanField()

class Upat(models.Model):
    pacient=models.ForeignKey(Pacienti, on_delete=models.CASCADE, null=True)
    doktor=models.ForeignKey(Doktori, on_delete=models.CASCADE, null=True)
    oddelenie=models.ForeignKey(Oddeli, on_delete=models.CASCADE, null=True)
    termin=models.DateTimeField(null=True, blank=True)
    zabeleshka=models.TextField()
    prioritet=models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.prioritet == True:
            za_kolku_vreme  = random.randint(1, 23)
            random_minuti = random.randint(1, 59)
            self.termin = now() + timedelta(hours=za_kolku_vreme, minutes=random_minuti)
            super(Upat, self).save(*args, **kwargs)

class Pregledi(models.Model):
    pacient=models.ForeignKey(Pacienti, on_delete=models.CASCADE, null=True)
    doktor=models.ForeignKey(Doktori, on_delete=models.CASCADE, null=True)
    oddelenie=models.ForeignKey(Oddeli, on_delete=models.CASCADE, null=True)
    datum_pregled=models.DateTimeField()
    zabeleshka=models.CharField(max_length=50, null=True)
    kontrola=models.IntegerField(null=True, blank=True)
    dijagnoza=models.TextField()
    terapija=models.TextField(null=True, blank=True)
    termin=models.ForeignKey(Upat, on_delete=models.CASCADE, null=True, blank=True)




