from django.shortcuts import render, HttpResponseRedirect
from. forms import FilmForm, SiteForm
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

def centre(request):
    liste = list(models.Film.objects.all())
    return render(request, "film/centre.html", {"liste": liste})
def index(request):
    liste = list(models.Film.objects.all())
    return render(request, "film/index.html", {"liste": liste})


def affiche(request, id):
    film = models.Film.objects.get( pk = id)
    return render(request, "film/affiche.html", {"film": film})

def update(request, id):
    film = models.Film.objects.get(pk=id)
    form = FilmForm(film.dico())
    return render(request,"film/ajout.html", {"form": form, "id": id})

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






#######################################



def ajoutsite(request):
    if request.method == "POST":
        form = SiteForm(request)
        return render(request, "film/ajoutsite.html", {"form": form})
    else :
        form = SiteForm()
        return render(request, "film/ajoutsite.html", {"form": form})

def revusite(request):
    lform = SiteForm(request.POST)
    if lform.is_valid():
        site = lform.save()
        return HttpResponseRedirect("/stream/")
    else :
        return render(request, "film/ajoutsite.html", {"form": lform})


def indexsite(request):
    liste = list(models.Site.objects.all())
    return render(request, "film/indexsite.html", {"liste": liste})


def affichesite(request, id):
    site = models.Site.objects.get( pk = id)
    return render(request, "film/affichesite.html", {"site": site})

def updatesite(request, id):
    site = models.Site.objects.get(pk=id)
    form = SiteForm(site.dico())
    return render(request,"film/ajoutsite.html", {"form": form, "id": id})

def updaterevusite(request, id):
    lform = SiteForm(request.POST)
    if lform.is_valid():
        site = lform.save(commit = False)
        site.id = id
        site.save()
        return HttpResponseRedirect("/stream/ajoutsite/")
    else:
        return render(request, "film/ajoutsite.html", {"form": lform, "id": id})

def deletesite(request, id):
    site = models.Site.objects.get(pk=id)
    site.delete()
    return HttpResponseRedirect("/stream/")



