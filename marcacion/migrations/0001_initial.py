# Generated by Django 5.1.1 on 2024-11-28 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(blank=True, max_length=2000, unique=True)),
                ('nombre', models.CharField(max_length=100)),
                ('dni', models.CharField(max_length=8)),
                ('horario_entrada', models.TimeField()),
                ('horario_salida', models.TimeField()),
                ('horario_refrigerio', models.TimeField()),
            ],
        ),
    ]
