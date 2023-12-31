# Generated by Django 4.1.3 on 2022-11-11 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Users",
            fields=[
                ("user_id", models.BigAutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=25)),
                ("username", models.CharField(max_length=25, unique=True)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("password", models.TextField(max_length=250)),
            ],
        ),
    ]
