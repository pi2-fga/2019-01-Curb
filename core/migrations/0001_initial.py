# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-06-03 18:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('codigo', models.IntegerField()),
                ('link', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=5)),
                ('hora', models.CharField(max_length=10)),
                ('data', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Monitoramento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tinta', models.IntegerField()),
                ('bateria', models.IntegerField()),
                ('latitude',  models.CharField(max_length=15)),
                ('logitude',  models.CharField(max_length=15)),
                ('hora',  models.CharField(max_length=10)),
                ('data',  models.CharField(max_length=10)),
                ('status', models.CharField(max_length=5)),

            ],
        ),
        migrations.CreateModel(
            name='Relatorio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hora', models.CharField(max_length=10)),
                ('data', models.CharField(max_length=10)),
                ('tintaAtual', models.IntegerField()),
                ('bateriaAtual', models.IntegerField()),
                ('consumoTinta', models.IntegerField()),
                ('consumoBateria', models.IntegerField()),


            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=5)),
                ('cpf', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='curb',
            name='usuarioAtivo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Usuario'),
        ),
        migrations.AddField(
            model_name='monitoramento',
            name='curbAtivo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Curb'),
        ),
        migrations.AddField(
            model_name='relatorio',
            name='curbAtivo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Curb'),
        ),
    ]