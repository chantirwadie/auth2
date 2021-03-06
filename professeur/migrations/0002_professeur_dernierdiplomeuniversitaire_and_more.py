# Generated by Django 4.0.2 on 2022-04-30 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('professeur', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='professeur',
            name='DernierDiplomeUniversitaire',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='professeur',
            name='ModulesEnseignes',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='professeur',
            name='Specialite',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='professeur',
            name='VilleDepart',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='professeur',
            name='dateNaissance',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='professeur',
            name='departement',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='professeur',
            name='grade',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
