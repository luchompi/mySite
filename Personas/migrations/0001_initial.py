# Generated by Django 4.0 on 2021-12-24 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('pseudonimo', models.CharField(error_messages={'unique': 'Ya existe un registro con este nombre'}, max_length=50, primary_key=True, serialize=False, unique=True, verbose_name='Nombre del Autor')),
                ('direccion', models.CharField(max_length=100, verbose_name='Direccion de Residencia')),
                ('correo', models.EmailField(max_length=254, verbose_name='Correo Electronico')),
                ('bio', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Autor',
                'verbose_name_plural': 'Autores',
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('iden', models.IntegerField(error_messages={'unique': 'Ya existe un cliente registrado con este ID'}, primary_key=True, serialize=False, unique=True, verbose_name='Identificacion')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre del Cliente')),
                ('apellidos', models.CharField(max_length=50, verbose_name='Apellidos del cliente')),
                ('direccion', models.CharField(max_length=100, verbose_name='Direccion de Residencia')),
                ('correo', models.EmailField(max_length=254, verbose_name='Correo Electronico')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
    ]
