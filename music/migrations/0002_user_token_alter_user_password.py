# Generated by Django 4.2.6 on 2023-10-28 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("music", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="token",
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name="user",
            name="password",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
