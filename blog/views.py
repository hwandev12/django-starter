from django.shortcuts import render
from .models import Cards, Andijon

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
    return render(request, 'namangan.html')

def buxoro(request):
    return render(request, 'buxoro.html')
