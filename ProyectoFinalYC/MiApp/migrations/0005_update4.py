# Generated by Django 4.2.1 on 2023-07-03 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MiApp', '0004_update3'),
    ]

    operations = [
        migrations.AddField(
            model_name='guias',
            name='subtitulo',
            field=models.CharField(default='', max_length=80),
        ),
        migrations.AddField(
            model_name='post',
            name='subtitulo',
            field=models.CharField(default='', max_length=80),
        ),
        migrations.AlterField(
            model_name='guias',
            name='titulo',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='post',
            name='titulo',
            field=models.CharField(max_length=50),
        ),
    ]