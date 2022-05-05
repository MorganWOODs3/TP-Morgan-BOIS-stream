from django.shortcuts import render, HttpResponseRedirect
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
        film = lform.save()
        return HttpResponseRedirect("/stream/")
    else :
        return render(request, "film/ajout.html", {"form": lform})


def index(request):
    liste = list(models.Film.objects.all())
    return render(request,"film/index.html",{"list" : liste})

def affiche(request, id):
    film = models.Film.objects.get( pk = id)
    return render(request,"film/ajout.html",{"film": film})

def update(request, id):
    film = models.Film.objects.get(pk=id)
    form = FilmForm(film.dico())
    return render(request,"film/ajout.html", {"from": form, "id": id})

def updaterevu(request, id):
    lform = FilmForm(request.POST)
    if lform.is_valid():
        film = lform.save(commit = False)
        film.id = id
        film.save()
        return HttpResponseRedirect("/stream/")
    else:
        return render(request, "film/ajout.html", {"form": lform, "id": id})

def delete(request, id):
    film = models.Film.objects.get(pk=id)
    film.delete()
    return HttpResponseRedirect("/stream/")



