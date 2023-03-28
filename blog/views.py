from django.shortcuts import render


def home(request):
    return render(request, 'index.html')


def andijon(request):
    return render(request, 'andijon.html')


def namangan(request):
    return render(request, 'namangan.html')

def buxoro(request):
    return render(request, 'buxoro.html')
