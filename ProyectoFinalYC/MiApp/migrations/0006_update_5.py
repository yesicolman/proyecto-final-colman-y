# Generated by Django 4.2.1 on 2023-07-04 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MiApp', '0005_update4'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuarios',
            name='mensaje',
            field=models.CharField(default='mensaje no encontrado', max_length=500),
        ),
    ]
