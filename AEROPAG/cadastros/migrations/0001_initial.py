# Generated by Django 5.1 on 2024-10-11 18:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('descricao', models.CharField(max_length=150, verbose_name='Descrição')),
            ],
        ),
        migrations.CreateModel(
            name='Atividade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField(verbose_name='Número')),
                ('descricao', models.CharField(max_length=150, verbose_name='Descrição')),
                ('pontos', models.DecimalField(decimal_places=1, max_digits=4)),
                ('detalhes', models.CharField(max_length=150)),
                ('turma', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.turma')),
            ],
        ),
    ]
