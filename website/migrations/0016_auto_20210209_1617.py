# Generated by Django 3.1.6 on 2021-02-09 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0015_auto_20210209_1608'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='bairro',
        ),
        migrations.RemoveField(
            model_name='post',
            name='cidade',
        ),
        migrations.RemoveField(
            model_name='post',
            name='email',
        ),
        migrations.RemoveField(
            model_name='post',
            name='endereco',
        ),
        migrations.RemoveField(
            model_name='post',
            name='nrTelCelular',
        ),
        migrations.RemoveField(
            model_name='post',
            name='numero',
        ),
    ]
