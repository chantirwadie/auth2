# Generated by Django 4.0.2 on 2022-04-28 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=120)),
                ('last_name', models.CharField(blank=True, max_length=120)),
                ('username', models.CharField(db_index=True, error_messages={'unique': 'The field Must be unique'}, max_length=255, unique=True)),
                ('email', models.EmailField(db_index=True, error_messages={'unique': "L'email existe deja"}, max_length=254, unique=True)),
                ('cin', models.CharField(blank=True, error_messages={'unique': 'CIN must be unique'}, max_length=12)),
                ('nationality', models.CharField(blank=True, max_length=60)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('role', models.CharField(choices=[('Etudiant', 'Etudiant'), ('Coordinateur', 'Coordinateur'), ('Staff', 'Staff'), ('TopManageur', 'TopManageur'), ('Professeur', 'Professeur')], max_length=50, null=True)),
                ('birth_date', models.DateField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
