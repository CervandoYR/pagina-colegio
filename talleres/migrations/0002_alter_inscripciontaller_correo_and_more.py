# Generated by Django 5.1.1 on 2024-11-01 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('talleres', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscripciontaller',
            name='correo',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='inscripciontaller',
            name='numero',
            field=models.CharField(max_length=9, unique=True),
        ),
    ]
