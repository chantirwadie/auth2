# Generated by Django 4.0.2 on 2022-05-02 04:40

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('resetPassword', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resetpassword',
            name='expired_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 2, 4, 55, 46, 718327)),
        ),
        migrations.AlterField(
            model_name='resetpassword',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reset_password_profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
