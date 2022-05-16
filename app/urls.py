from django.urls import path
from .views import DoktoriView, PacientiView, HospitalizacijaView, OddeliView, PreglediView, GithubConnect
from allauth.socialaccount.providers.github import views as github_views

urlpatterns = [
    path('doktori/', DoktoriView.as_view()),
    path('pacienti/', PacientiView.as_view()),
    path('pregledi/', PreglediView.as_view()),
    path('hospitalizacija/', HospitalizacijaView.as_view()),
    path('oddeli/', OddeliView.as_view()),
    path('github/', GithubConnect.as_view()),
    path('github/auth/', github_views.oauth2_login)
    

]