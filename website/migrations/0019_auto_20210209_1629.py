# Generated by Django 3.1.6 on 2021-02-09 19:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0018_auto_20210209_1626'),
    ]

    operations = [
        migrations.RenameField(
            model_name='perfil',
            old_name='endereço',
            new_name='endereco',
        ),
    ]
