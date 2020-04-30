# Generated by Django 3.0.5 on 2020-04-29 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_de_cuenta', models.PositiveIntegerField(unique=True)),
                ('nombre', models.CharField(max_length=50)),
                ('primer_apellido', models.CharField(max_length=50)),
                ('segundo_apellido', models.CharField(max_length=50)),
                ('carrera', models.CharField(max_length=20)),
                ('semestre', models.PositiveIntegerField(default=0)),
                ('promedio', models.FloatField(default=0)),
                ('al_corriente', models.BooleanField(default=True)),
            ],
        ),
    ]
