# Generated by Django 5.0.1 on 2024-01-18 09:04

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendence_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendencedata',
            name='now_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]