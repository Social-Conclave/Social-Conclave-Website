from django.urls import path, include
from . import views
from django.views.generic import TemplateView

app_name = 'main'

urlpatterns = [
    path('', views.home, name='landing-page'),
    path('team/', views.team, name="team"),
    path('agendas', views.agendas, name="agendas"),
    path('EducationAUniversalRight', views.EducationAUniversalRight, name="EducationAUniversalRight"),
    path('ReproductiveHealthAndRights', views.ReproductiveHealthAndRights, name="ReproductiveHealthAndRights"),
    path('DrugRehabilitationAndRecovery', views.DrugRehabilitationAndRecovery, name="DrugRehabilitationAndRecovery"),
    path('WildlifeAndEcosystemProtection', views.WildlifeAndEcosystemProtection, name="WildlifeAndEcosystemProtection")
]

