# Generated by Django 4.2.1 on 2023-06-22 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MiApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=40)),
                ('contenido', models.CharField(max_length=300)),
                ('fecha_publicacion', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Guias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autor', models.CharField(max_length=20)),
                ('titulo', models.CharField(max_length=40)),
                ('destino', models.CharField(max_length=40)),
                ('pais', models.CharField(max_length=40)),
                ('contenido', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Respuesta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=40)),
                ('contenido', models.CharField(max_length=300)),
                ('fecha_publicacion', models.DateTimeField()),
            ],
        ),
        migrations.RenameField(
            model_name='post',
            old_name='Contenido',
            new_name='contenido',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='Titulo',
            new_name='titulo',
        ),
    ]
