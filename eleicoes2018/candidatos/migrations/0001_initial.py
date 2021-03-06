# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2018-11-30 16:00
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
                ('nome_completo', models.CharField(help_text='Nome completo', max_length=125)),
                ('nome_urna', models.CharField(help_text='Nome na urna eletrônica', max_length=75)),
                ('genero', models.CharField(help_text='Gênero', max_length=35)),
                ('grau_instrucao', models.CharField(help_text='Escolaridade', max_length=40)),
                ('estado_civil', models.CharField(help_text='Estado civil', max_length=40)),
                ('idade_data_posse', models.IntegerField(help_text='Idade na data da posse')),
                ('raca', models.CharField(help_text='Raça', max_length=50)),
                ('ocupacao', models.CharField(help_text='Ocupação', max_length=80)),
                ('email_contato', models.EmailField(help_text='E-mail', max_length=254)),
                ('nacionalidade', models.CharField(help_text='Nacionalidade', max_length=50)),
                ('data_nasc', models.DateField(help_text='Data de nascimento')),
                ('numero_candidato', models.IntegerField(help_text='Número do candidato')),
            ],
            options={
                'verbose_name_plural': 'Candidatos',
            },
        ),
        migrations.CreateModel(
            name='Candidatura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reeleicao', models.CharField(help_text='Candidato disputa a reeleição? (S/N)', max_length=1)),
                ('declaracao_bens', models.CharField(help_text='Candidato declarou bens? (S/N)', max_length=1)),
                ('resultado_eleicao', models.CharField(default='nao eleito', help_text='Situação do candidato na eleição', max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Candidaturas',
            },
        ),
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc_cargo', models.CharField(help_text='Cargo pelo qual o candidato está concorrendo', max_length=100, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Cargos',
            },
        ),
        migrations.CreateModel(
            name='Coligacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_coligacao', models.CharField(help_text='Nome da coligação de partidos', max_length=200)),
                ('candidatos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='candidatos.Candidato')),
            ],
            options={
                'verbose_name': 'Coligação',
                'verbose_name_plural': 'Coligações',
            },
        ),
        migrations.CreateModel(
            name='Coligacao_Partidos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coligacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='candidatos.Coligacao')),
            ],
            options={
                'verbose_name_plural': 'Coligações e Partidos',
            },
        ),
        migrations.CreateModel(
            name='Eleicao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc_eleicao', models.CharField(help_text='Descrição', max_length=100)),
                ('ano_eleicao', models.IntegerField(help_text='Ano da eleição')),
                ('abrangencia', models.CharField(help_text='Estadual ou Federal', max_length=30)),
            ],
            options={
                'verbose_name': 'Eleição',
                'verbose_name_plural': 'Eleições',
            },
        ),
        migrations.CreateModel(
            name='Estado_Nascimento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UF', models.CharField(help_text='Estado de origem do candidato', max_length=3, unique=True)),
            ],
            options={
                'verbose_name': 'Estado',
                'verbose_name_plural': 'Estados',
            },
        ),
        migrations.CreateModel(
            name='Local_Eleicao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('abreviacao', models.CharField(max_length=3)),
                ('nome_local', models.CharField(help_text='Local onde a eleição é disputada', max_length=50)),
                ('eleicao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='candidatos.Eleicao')),
            ],
            options={
                'verbose_name_plural': 'Locais de eleição',
            },
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_municipio', models.CharField(help_text='Município de nascimento do candidato', max_length=100, unique=True)),
                ('UF', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='candidatos.Estado_Nascimento')),
            ],
            options={
                'verbose_name': 'Município',
                'verbose_name_plural': 'Municípios',
            },
        ),
        migrations.CreateModel(
            name='Partido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sigla_partido', models.CharField(help_text='Sigla do partido', max_length=10, unique=True)),
                ('nome_partido', models.CharField(help_text='Nome do partido', max_length=50)),
                ('numero_partido', models.IntegerField(help_text='Número do partido na urna')),
            ],
            options={
                'verbose_name_plural': 'Partidos',
            },
        ),
        migrations.CreateModel(
            name='Turno_Eleicao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_eleicao', models.DateField(help_text='Data da eleição')),
                ('turno', models.IntegerField(help_text='1º ou 2º turno')),
                ('eleicao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='candidatos.Eleicao')),
            ],
            options={
                'verbose_name_plural': 'Turnos da Eleição',
            },
        ),
        migrations.AddField(
            model_name='coligacao_partidos',
            name='partido',
            field=models.ManyToManyField(to='candidatos.Partido'),
        ),
        migrations.AddField(
            model_name='coligacao',
            name='local',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='candidatos.Local_Eleicao'),
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
            name='local_eleicao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='candidatos.Local_Eleicao'),
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
