# Generated by Django 4.0.2 on 2022-05-17 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coordinateur', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coordinateur',
            name='image',
            field=models.ImageField(default='images/default.png', upload_to='images/'),
        ),
    ]
