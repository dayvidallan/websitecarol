# Generated by Django 3.1.6 on 2021-02-03 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_auto_20210203_1425'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='especialidade',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='perfil',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='perfil',
            name='nrTelCelular',
            field=models.CharField(blank=True, max_length=11, null=True, verbose_name='Nº telefone celular'),
        ),
    ]