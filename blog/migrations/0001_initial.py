# Generated by Django 4.1.1 on 2022-10-05 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Articulo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("titulo", models.DateField(max_length=50)),
                ("fecha", models.DateField()),
                ("texto", models.CharField(max_length=300)),
            ],
            options={
                "verbose_name": "Articulo",
                "verbose_name_plural": "Articulos",
            },
        ),
        migrations.CreateModel(
            name="Autor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=30)),
                ("apellido", models.CharField(max_length=30)),
                ("email", models.EmailField(max_length=250)),
            ],
            options={
                "verbose_name": "Autor",
                "verbose_name_plural": "Autores",
            },
        ),
        migrations.CreateModel(
            name="Seccion",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("categoria", models.CharField(max_length=30)),
            ],
            options={
                "verbose_name": "Seccion",
                "verbose_name_plural": "Secciones",
            },
        ),
    ]
