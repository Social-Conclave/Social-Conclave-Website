from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse
from .models import Member, Agenda
from django.conf import settings
import json
app_name = "core"


def agendas(request):
    return render(request, 'core/agendas.html')


def overTheYears(request):
    return render(request, 'core/overTheYears.html')

def EducationAUniversalRight(request):
    apikey = settings.GOOGLE_API_KEY
    data = {
        'key':apikey,
    }
    return render(request, 'core/EducationAUniversalRight.html', data)

def ReproductiveHealthAndRights(request):
    apikey = settings.GOOGLE_API_KEY
    data = {
        'key':apikey,
    }
    return render(request, 'core/ReproductiveHealthAndRights.html', data)

def DrugRehabilitationAndRecovery(request):
    apikey = settings.GOOGLE_API_KEY
    data = {
        'key':apikey,
    }
    return render(request, 'core/DrugRehabilitationAndRecovery.html', data)

def WildlifeAndEcosystemProtection(request):
    apikey = settings.GOOGLE_API_KEY
    data = {
        'key':apikey,
    }
    return render(request, 'core/WildlifeAndEcosystemProtection.html', data)
