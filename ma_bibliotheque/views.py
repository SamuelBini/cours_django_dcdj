from django.shortcuts import render
from .models import Livre

# Create your views here.
def recherche_page(request):
    mesLivrres = Livre.objects.filter()
    return render(request, "ma_bibliotheque/recherche_page.html", {'livres' : mesLivrres})