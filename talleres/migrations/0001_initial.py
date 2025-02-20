# Generated by Django 5.1.1 on 2024-10-04 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InscripcionTaller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('correo', models.EmailField(max_length=254)),
                ('numero', models.CharField(max_length=15)),
                ('apoderado', models.CharField(max_length=100)),
                ('grado', models.CharField(max_length=10)),
                ('seccion', models.CharField(max_length=10)),
                ('taller', models.CharField(choices=[('ajedrez', 'Taller de Ajedrez'), ('teatro', 'Taller de Teatro'), ('oratoria', 'Taller de Oratoria'), ('danza', 'Taller de Danza')], max_length=20)),
                ('horario', models.CharField(max_length=50)),
            ],
        ),
    ]
