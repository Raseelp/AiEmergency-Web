# Generated by Django 3.2.25 on 2025-02-16 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0005_remove_patient_table_placedetails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location_table',
            name='Latitude',
            field=models.CharField(max_length=100),
        ),
    ]
