# Generated by Django 5.1.2 on 2024-10-27 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('cli_codigo', models.AutoField(primary_key=True, serialize=False)),
                ('cli_cliente', models.CharField(max_length=255)),
                ('cli_email', models.EmailField(max_length=255)),
                ('cli_telefone', models.CharField(max_length=50)),
                ('cli_avi_codigo', models.IntegerField()),
            ],
        ),
    ]
