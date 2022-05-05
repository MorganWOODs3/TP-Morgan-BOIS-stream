from django.db import models


# Create your models here.
class Film(models.Model):
    titre = models.CharField(max_length=100)
    realisateur = models.CharField(max_length=100)
    date_parution = models.DateField(blank=True, null=True)
    dure = models.IntegerField(blank=False)
    resume = models.TextField(null=True, blank=True)

    def __str__(self):
        chaine= f"{self.titre} écrit par {self.realisateur} et avec {self.dure} minutes, édité le {self.date_parution} et voici le résumer {self.resume}."
        return chaine