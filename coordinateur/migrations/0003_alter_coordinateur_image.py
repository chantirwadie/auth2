# Generated by Django 4.0.2 on 2022-05-18 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coordinateur', '0002_coordinateur_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coordinateur',
            name='image',
            field=models.ImageField(default='images/coordinateur/default.png', upload_to='images/'),
        ),
    ]