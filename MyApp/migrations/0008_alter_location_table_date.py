# Generated by Django 3.2.25 on 2025-02-16 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0007_alter_location_table_longitude'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location_table',
            name='date',
            field=models.CharField(max_length=100),
        ),
    ]
