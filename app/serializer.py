from rest_framework import serializers
from .models import Pacienti, Doktori, Oddeli, Pregledi, Hospitalizacija, Upat


class PacientiSerializer(serializers.ModelSerializer):

    class Meta:
        model=Pacienti
        fields='__all__'
    
    def create(self, validated_data):
        return Pacienti.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)

class DoktoriSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Doktori
        fields='__all__'
    
    def create(self, validated_data):
        return Doktori.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)

class OddeliSerializer(serializers.ModelSerializer):

    class Meta:
        model=Oddeli
        fields='__all__'

    def create(self, validated_data):
        return Oddeli.objects.create(**validated_data)

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)

class UpatSerializer(serializers.ModelSerializer):

    class Meta:
        model=Upat
        fields='__all__'

    def create(self, validated_data):
        return Upat.objects.create(**validated_data)

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)

class PreglediSerializer(serializers.ModelSerializer):
    doktor=DoktoriSerializer(read_only=True)
    pacient=PacientiSerializer(read_only=True)

    class Meta:
        model=Pregledi
        fields='__all__'

        def create(self, validated_data):
            return Pregledi.objects.create(**validated_data)

        def update(self, instance, validated_data):
            return super().update(instance, validated_data)

class HospitalizacijaSerializer(serializers.ModelSerializer):

    class Meta:
        model=Hospitalizacija
        fields='__all__'

    def create(self, validated_data):
        return Hospitalizacija.objects.create(**validated_data)

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)


