# Generated by Django 3.1.6 on 2021-02-03 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_perfil'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='perfils'),
        ),
    ]
