# Generated by Django 3.2.25 on 2025-01-04 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0002_notification_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_message_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EmergencyMessage', models.CharField(max_length=100)),
                ('Date', models.DateField()),
                ('Time', models.TimeField()),
                ('Latitude', models.FloatField()),
                ('Longitude', models.FloatField()),
            ],
        ),
    ]
