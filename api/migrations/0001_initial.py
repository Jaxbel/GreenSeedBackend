# Generated by Django 4.1.1 on 2022-12-06 06:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Planta",
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
                ("name", models.CharField(max_length=100)),
                ("about", models.TextField()),
                ("ilumination", models.TextField()),
                ("irrigation", models.TextField()),
                ("irrigation_p1", models.CharField(max_length=100)),
                ("irrigation_p2", models.CharField(max_length=100)),
                ("irrigation_p3", models.CharField(max_length=100)),
                ("substratum", models.TextField()),
                ("substratum_p1", models.CharField(max_length=100)),
                ("substratum_p2", models.CharField(max_length=100)),
                ("substratum_p3", models.CharField(max_length=100)),
                ("substratum_p4", models.CharField(max_length=100)),
                ("substratum_p5", models.CharField(max_length=100)),
                ("temperature", models.TextField()),
                ("reproduction", models.TextField()),
                ("reproduction_leaf", models.TextField()),
                ("reproduction_sprout", models.TextField()),
                ("reproduction_seeds", models.TextField()),
                ("image", models.ImageField(blank=True, null=True, upload_to="plants")),
            ],
        ),
        migrations.CreateModel(
            name="PlantaData",
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
                ("title", models.CharField(max_length=100)),
                ("description", models.TextField()),
                (
                    "planta",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="planta_data",
                        to="api.planta",
                    ),
                ),
            ],
        ),
    ]
