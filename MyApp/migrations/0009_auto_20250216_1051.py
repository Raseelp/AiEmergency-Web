# Generated by Django 3.2.25 on 2025-02-16 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0008_alter_location_table_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='ambulance_request_table',
            name='latitude',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ambulance_request_table',
            name='longitude',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
