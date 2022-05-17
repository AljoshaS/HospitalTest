from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Doktori, Pacienti, Pregledi, Hospitalizacija, Oddeli
from .serializer import DoktoriSerializer, PacientiSerializer, PreglediSerializer, HospitalizacijaSerializer, OddeliSerializer
from rest_framework.permissions import IsAuthenticated
from allauth.socialaccount.providers.github import views as github_views
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from allauth.socialaccount.providers.github.views import GitHubOAuth2Adapter
from dj_rest_auth.registration.views import SocialConnectView
from django.views.generic import TemplateView

# Create your views here.

class DoktoriView(APIView):

    permission_classes=(IsAuthenticated,)
    
    def get(self, request):
        doktor = Doktori.objects.get(id=request.GET['doktorId'])
        doktor_serializer = DoktoriSerializer(doktor)
        return Response(doktor_serializer.data)

    def post(self, request):
        doktor_serializer = DoktoriSerializer(data= request.data)
        if doktor_serializer.is_valid():
            doktor_serializer.save()
            return Response(doktor_serializer.data)
        return Response({"error": "nastana nekoj error"}, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        doktor = Doktori.objects.get(id=request.GET['doktorId'])
        doktor.delete()
        return Response({"info": "Doktorot e izbrisan"})

    def patch(self, request):
        doktori=Doktori.objects.get(id=request.data['id'])
        doktori_serializer=DoktoriSerializer(doktori, data=request.data)
        if doktori_serializer.is_valid():
            doktori_serializer.save()
            return Response(doktori_serializer.data, status=status.HTTP_400_BAD_REQUEST)
        return Response({"errors":doktori_serializer.errors})

class PacientiView(APIView):

    def get(self, request):
        pacient = Pacienti.objects.get(id=request.GET['pacientId'])
        pacient_serializer = PacientiSerializer(pacient)
        return Response(pacient_serializer.data)

    def post(self, request):
        pacient_serializer = PacientiSerializer(data= request.data)
        if pacient_serializer.is_valid():
            pacient_serializer.save()
            return Response(pacient_serializer.data)
        return Response({"error": "nastana nekoj error"}, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        pacient = Pacienti.objects.get(id=request.GET['pacientId'])
        pacient.delete()
        return Response({"info": "Pacientot e izbrisan"})

    def patch(self, request):
        pacienti=Pacienti.objects.get(id=request.data['id'])
        pacienti_serializer=PacientiSerializer(pacienti, data=request.data)
        if pacienti_serializer.is_valid():
            pacienti_serializer.save()
            return Response(pacienti_serializer, status=status.HTTP_400_BAD_REQUEST)
        return Response({"errors":pacienti_serializer.data.errors})

class HospitalizacijaView(APIView):

    def get(self, request):
        hospitalizacija = Hospitalizacija.objects.get(id=request.GET['hospitalizacijaId'])
        hospitalizacija_serializer = HospitalizacijaSerializer(hospitalizacija)
        return Response(hospitalizacija_serializer.data)

    def post(self, request):
        hospitalizacija_serializer = HospitalizacijaSerializer(data= request.data)

        if hospitalizacija_serializer.is_valid():
            hospitalizacija_serializer.save()
            return Response(hospitalizacija_serializer.data)
        return Response({"error":hospitalizacija_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        hospitalizacija = Hospitalizacija.objects.get(id=request.GET['hospitalizacijaId'])
        hospitalizacija.delete()
        return Response({"info": "Hospitalizacijata e izbrishana"})

    def patch(self, request):
        hospitalizacija=Hospitalizacija.objects.get(id=request.data['id'])
        hospitalizacija_serializer=HospitalizacijaSerializer(hospitalizacija, data=request.data)
        if hospitalizacija_serializer.is_valid():
            hospitalizacija_serializer.save()
            return Response(hospitalizacija_serializer.data, status=status.HTTP_400_BAD_REQUEST)
        return Response({"errors":hospitalizacija_serializer.errors})

class OddeliView(APIView):

    def get(self, request):
        oddel = Oddeli.objects.get(id=request.GET['oddelId'])
        oddel_serializer = OddeliSerializer(oddel)
        return Response(oddel_serializer.data)

    def post(self, request):
        oddel_serializer = OddeliSerializer(data= request.data)
        if oddel_serializer.is_valid():
            oddel_serializer.save()
            return Response(oddel_serializer.data)
        return Response({"error": "nastana nekoj error"}, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        oddel = Oddeli.objects.get(id=request.GET['oddelId'])
        oddel.delete()
        return Response({"info": "Oddelot e izbrisan"})

    def patch(self, request):
        oddel=Oddeli.objects.get(id=request.data['id'])
        oddel_serializer=PreglediSerializer(oddel, data=request.data)
        if oddel_serializer.is_valid():
            oddel_serializer.save()
            return Response(oddel_serializer.data, status=status.HTTP_400_BAD_REQUEST)
        return Response({"errors":oddel_serializer.errors})

class PreglediView(APIView):

    def get(self, request):
        pregled = Pregledi.objects.get(id=request.GET['pregledId'])
        pregled_serializer = PreglediSerializer(pregled)
        return Response(pregled_serializer.data)

    def post(self, request):
        pregled_serializer = PreglediSerializer(data= request.data)
        if pregled_serializer.is_valid():
            pregled_serializer.save()
            return Response(pregled_serializer.data)
        return Response({"error": pregled_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        pregled = Pregledi.objects.get(id=request.GET['pregledId'])
        pregled.delete()
        return Response({"info": "Pregledot e izbrisan"})

    def patch(self, request):
        pregled=Pregledi.objects.get(id=request.data['id'])
        pregled_serializer=PreglediSerializer(pregled, data=request.data)
        if pregled_serializer.is_valid():
            pregled_serializer.save()
            return Response(pregled_serializer.data, status=status.HTTP_400_BAD_REQUEST)
        return Response({"errors":pregled_serializer.errors})

class GithubConnect(SocialConnectView):
    adapter_class = GitHubOAuth2Adapter
    callback_url = "http://127.0.0.1:800/github/"
    client_class = OAuth2Client

class Home(TemplateView):
    template_name = "home.html"



