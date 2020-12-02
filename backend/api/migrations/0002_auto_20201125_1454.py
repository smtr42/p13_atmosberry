# Generated by Django 3.1.3 on 2020-11-25 14:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="sensor",
            name="reading",
        ),
        migrations.AddField(
            model_name="reading",
            name="sensor",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="sensor_reading",
                to="api.sensor",
            ),
            preserve_default=False,
        ),
    ]