from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class FilmForm(ModelForm):
    class Meta:
        model = models.Film
        fields = ('titre', 'realisateur', 'date_parution','dure','resume','cat','imaurl','site',)
        labels = {
            'titre': _('Titre'),
            'realisateur': _('Réalisateur'),
            'date_parution': _('Date de parution'),
            'dure': _('Duré du film en minutes'),
            'remume': _('Résumé'),
            'cat': _('Catégorie'),
            'imaurl': _('Image avec Url'),
            'site': _('Site streaming où on le trouve')

        }

class SiteForm(ModelForm):
    class Meta:
        model = models.Site
        fields = ('titre', 'url', 'resume')
        labels = {
            'titre': _('Titre'),
            'url': _('URL'),
            'resume': _('Résumé')
        }
