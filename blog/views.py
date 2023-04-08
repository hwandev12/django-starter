from django.shortcuts import render
from .models import Cards, Andijon, Namangan

def home(request):
    cards = Cards.objects.all()
    context = {
        "cards": cards
    }
    return render(request, 'index.html', context)


def andijon(request):
    andijon = Andijon.objects.all()
    context = {
        "andijon": andijon
    }
    return render(request, 'andijon.html', context)


def namangan(request):
    namangan = Namangan.objects.all()
    context = {
        "namangan": namangan
    }
    return render(request, 'namangan.html', context)

def buxoro(request):
    return render(request, 'buxoro.html')
