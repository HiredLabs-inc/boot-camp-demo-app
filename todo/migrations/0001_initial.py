# Generated by Django 5.0.6 on 2024-07-05 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Task",
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
                ("due", models.DateField()),
                (
                    "status",
                    models.CharField(
                        choices=[("Complete", "Complete"), ("To Do", "To Do")],
                        default="To Do",
                        max_length=30,
                    ),
                ),
            ],
        ),
    ]
