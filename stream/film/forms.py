from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class FilmForm(ModelForm):
    class Meta:
        model = models.Film
        fields = ('titre', 'realisateur', 'date_parution','dure','resume')
        labels = {
            'titre': _('Titre'),
            'realisateur': _('Réalisateur'),
            'date_parution': _('Date de parution'),
            'dure': _('Duré du film'),
            'remume': _('Résumé')
        }

class VadrazForm(ModelForm):
    class Meta:
        model = models.Film
        fields = ('titre', 'url')
        labels = {
            'titre': _('Titre'),
            'url': _('Réalisateur'),
            'date_parution': _('Date de parution'),
            'dure': _('Duré du film'),
            'remume': _('Résumé')
        }