# Generated by Django 4.2.11 on 2024-05-08 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("job_hunters", "0007_application_applied_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="companyprofile",
            name="name",
            field=models.CharField(max_length=255, unique=True),
        ),
    ]