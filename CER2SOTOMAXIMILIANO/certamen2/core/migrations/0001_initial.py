# Generated by Django 4.1.3 on 2022-11-13 17:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Residencia',
            fields=[
                ('numero', models.IntegerField(primary_key=True, serialize=False)),
                ('dueno', models.CharField(max_length=40)),
                ('telefono', models.IntegerField()),
                ('correo', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Correspondencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_recepcion', models.DateField(blank=True, null=True)),
                ('conserje', models.CharField(max_length=50)),
                ('remitente', models.CharField(max_length=50)),
                ('destinatario', models.CharField(max_length=50)),
                ('estado', models.CharField(max_length=30)),
                ('numresidencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.residencia')),
            ],
        ),
    ]
