# Generated by Django 4.0.4 on 2022-05-06 11:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0003_film_dico'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='film',
            name='dico',
        ),
    ]