# Generated by Django 4.0.6 on 2022-07-22 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fyp', '0025_alter_temproryresidentdata_car_plate_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='history',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Guest_id', models.BigIntegerField()),
                ('Exit_time', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
