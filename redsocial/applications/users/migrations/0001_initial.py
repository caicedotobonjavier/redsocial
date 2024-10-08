# Generated by Django 5.1 on 2024-08-13 18:19

import uuid
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
                ('user_id', models.UUIDField(default=uuid.uuid4, editable=False, verbose_name='Id usuario')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Correo electronico')),
                ('full_name', models.CharField(max_length=100, verbose_name='Nombre completo')),
                ('phone', models.CharField(blank=True, max_length=15, null=True, verbose_name='Telefono')),
                ('address', models.CharField(blank=True, max_length=50, null=True, verbose_name='Direccion')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='photo-perfil', verbose_name='Foto')),
                ('date_birth', models.DateField(blank=True, null=True, verbose_name='Fehca nacimiento')),
                ('cod_active', models.CharField(blank=True, max_length=6, verbose_name='Codigo Activacion')),
                ('otp_base32', models.CharField(blank=True, max_length=225, null=True)),
                ('login_otp', models.CharField(blank=True, max_length=255, null=True)),
                ('user_login_otp', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False, verbose_name='Staff')),
                ('is_active', models.BooleanField(default=False, verbose_name='Activo')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
