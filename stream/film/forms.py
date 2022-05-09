from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class FilmForm(ModelForm):
    class Meta:
        model = models.Film
        fields = ('titre', 'realisateur', 'date_parution','dure','resume','cat')
        labels = {
            'titre': _('Titre'),
            'realisateur': _('Réalisateur'),
            'date_parution': _('Date de parution'),
            'dure': _('Duré du film'),
            'remume': _('Résumé'),
            'cat': _('Catégorie')
        }

class SiteForm(ModelForm):
    class Meta:
        model = models.Site
        fields = ('titre', 'url')
        labels = {
            'titre': _('Titre'),
            'url': _('URL')
        }