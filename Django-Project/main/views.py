from django.shortcuts import render
from django.conf import settings

# Create your views here.


def home(request):
    return render(request, 'main/index.html')

def agendas(request):
    return render(request, 'agendas/agendas.html')

def team(request):
    return render(request, 'main/team.html')

def EducationAUniversalRight(request):
    apikey = settings.GOOGLE_API_KEY
    data = {
        'key':apikey,
    }
    return render(request, 'agendas/EducationAUniversalRight.html', data)

def ReproductiveHealthAndRights(request):
    apikey = settings.GOOGLE_API_KEY
    data = {
        'key':apikey,
    }
    return render(request, 'agendas/ReproductiveHealthAndRights.html', data)

def DrugRehabilitationAndRecovery(request):
    apikey = settings.GOOGLE_API_KEY
    data = {
        'key':apikey,
    }
    return render(request, 'agendas/DrugRehabilitationAndRecovery.html', data)

def WildlifeAndEcosystemProtection(request):
    apikey = settings.GOOGLE_API_KEY
    data = {
        'key':apikey,
    }
    return render(request, 'agendas/WildlifeAndEcosystemProtection.html', data)