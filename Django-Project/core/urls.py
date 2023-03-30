from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "core"

urlpatterns = [
    path('', views.overTheYears, name="overTheYears"),
    path('agendas', views.agendas, name="agendas"),
    path('EducationAUniversalRight', views.EducationAUniversalRight, name="EducationAUniversalRight"),
    path('ReproductiveHealthAndRights', views.ReproductiveHealthAndRights, name="ReproductiveHealthAndRights"),
    path('DrugRehabilitationAndRecovery', views.DrugRehabilitationAndRecovery, name="DrugRehabilitationAndRecovery"),
    path('WildlifeAndEcosystemProtection', views.WildlifeAndEcosystemProtection, name="WildlifeAndEcosystemProtection")
]
