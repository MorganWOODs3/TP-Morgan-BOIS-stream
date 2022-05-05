from django.shortcuts import render
from. forms import FilmForm
from . import models

# Create your views here.
def ajout(request):
    if request.method == "POST":
        form = FilmForm(request)
        return render(request, "film/ajout.html", {"form": form})
    else :
        form = FilmForm()
        return render(request, "film/ajout.html", {"form": form})

def revu(request):
    lform = FilmForm(request.POST)
    if lform.is_valid():
        livre = lform.save()
        return render(request, "film/revu.html", {"film": livre})
    else :
        return render(request, "film/ajout.html", {"form": lform})


def index(request):
    liste = list(models.Film.objects.all())
    return render(request,"film/index.html",{"list" : liste})