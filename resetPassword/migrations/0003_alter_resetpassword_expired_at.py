# Generated by Django 4.0.2 on 2022-05-03 14:03
# Generated by Django 4.0.2 on 2022-05-03 18:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('resetPassword', '0002_alter_resetpassword_expired_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resetpassword',
            name='expired_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 3, 18, 30, 39, 697493, tzinfo=utc)),
        ),
    ]
