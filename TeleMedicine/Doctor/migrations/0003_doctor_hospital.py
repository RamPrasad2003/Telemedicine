# Generated by Django 4.2.5 on 2024-02-12 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Doctor", "0002_appointment"),
    ]

    operations = [
        migrations.AddField(
            model_name="doctor",
            name="hospital",
            field=models.CharField(max_length=50, null=True),
        ),
    ]