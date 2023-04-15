from django.shortcuts import render
from .models import *

def home(request):

    category = request.GET.get("category")

    if category == None:
        cards = Cards.objects.all()
    else:
        cards = Cards.objects.filter(category__name=category)

    categories = Category.objects.all()
    context = {
        "cards": cards,
        "categories": categories
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
    buxoro_malumot = Buxoro.objects.all()
    context = {
        "buxoro_content": buxoro_malumot
    }
    return render(request, 'buxoro.html', context)

def books(request):
    book = Books.objects.all()
    return render(request, 'books.html', {"book": book})
