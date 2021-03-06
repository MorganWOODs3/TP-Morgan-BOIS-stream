# Generated by Django 4.0.4 on 2022-05-10 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0006_film_cat'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='resume',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='film',
            name='cat',
            field=models.CharField(choices=[('Ac', 'Action'), ('An', 'Animation'), ('Av', 'Aventure'), ('Ho', 'Horreur'), ('Fa', 'Fantastique'), ('Sf', 'Science Fiction'), ('Ge', 'Guerre')], max_length=30),
        ),
    ]
