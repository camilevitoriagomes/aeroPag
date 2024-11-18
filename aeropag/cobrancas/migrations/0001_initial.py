# Generated by Django 5.1.2 on 2024-11-18 17:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cobranca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cob_codigo', models.CharField(max_length=20)),
                ('tar_codigo', models.CharField(max_length=20)),
                ('quantidade_horas', models.IntegerField()),
                ('valor_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('data', models.DateField()),
                ('avi_codigo', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Tarifa',
            fields=[
                ('tar_codigo', models.AutoField(primary_key=True, serialize=False)),
                ('tar_tipo', models.CharField(max_length=255)),
                ('tar_valor_domestico', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tar_valor_internacional', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tar_grupo', models.IntegerField()),
                ('tar_ton_min', models.IntegerField()),
                ('tar_ton_max', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Aviao',
            fields=[
                ('avi_codigo', models.AutoField(primary_key=True, serialize=False)),
                ('avi_prefixo_do_aviao', models.CharField(max_length=50)),
                ('avi_toneladas', models.DecimalField(decimal_places=2, max_digits=10)),
                ('avi_grupo', models.IntegerField()),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cobrancas_usuario', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
