from django.urls import path
from . import views

urlpatterns = [
    path('', views.recherche_page, name="recherche_page")
]