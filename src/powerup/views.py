from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

def vue_de_test(request):
    return HttpResponse("<h1> Ceci est un test </h1>")

def index(request):
    date = datetime.today()
    print(date)
    return render(request, 'index.html', context={"prenom": "Jean", "date": date})