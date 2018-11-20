# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2018-11-20 01:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_completo', models.CharField(max_length=125)),
                ('nome_urna', models.CharField(max_length=75)),
                ('genero', models.CharField(max_length=35)),
                ('grau_instrucao', models.CharField(max_length=40)),
                ('estado_civil', models.CharField(max_length=40)),
                ('idade_data_posse', models.IntegerField()),
                ('raca', models.CharField(max_length=50)),
                ('ocupacao', models.CharField(max_length=80)),
                ('email_contato', models.EmailField(max_length=254)),
                ('nacionalidade', models.CharField(max_length=50)),
                ('data_nasc', models.DateField()),
                ('numero_candidato', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Candidatura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reeleicao', models.CharField(max_length=1)),
                ('declaracao_bens', models.CharField(max_length=1)),
                ('resultado_turno', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc_cargo', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Coligacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_coligacao', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Eleicao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('turno', models.IntegerField()),
                ('desc_eleicao', models.CharField(max_length=50)),
                ('data_eleicao', models.DateField()),
                ('ano_eleicao', models.IntegerField()),
                ('abrangencia', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Local_Nascimento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Localidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sigla_localidade', models.CharField(max_length=2)),
                ('local', models.CharField(max_length=75)),
                ('eleicao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='candidatos.Eleicao')),
            ],
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('municipio', models.CharField(max_length=75)),
            ],
        ),
        migrations.CreateModel(
            name='Partido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sigla_partido', models.CharField(max_length=2)),
                ('nome_partido', models.CharField(max_length=50)),
                ('numero_partido', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='local_nascimento',
            name='municipio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='candidatos.Municipio'),
        ),
        migrations.AddField(
            model_name='local_nascimento',
            name='sigla_localidade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='candidatos.Localidade'),
        ),
        migrations.AddField(
            model_name='coligacao',
            name='sigla_partido',
            field=models.ManyToManyField(to='candidatos.Partido'),
        ),
        migrations.AddField(
            model_name='candidato',
            name='candidatura',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='candidatos.Candidatura'),
        ),
        migrations.AddField(
            model_name='candidato',
            name='cargo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='candidatos.Cargo'),
        ),
        migrations.AddField(
            model_name='candidato',
            name='municipio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='candidatos.Municipio'),
        ),
        migrations.AddField(
            model_name='candidato',
            name='partido',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='candidatos.Partido'),
        ),
    ]
