# Generated by Django 4.0.6 on 2022-07-22 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fyp', '0033_guests_isentered'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='Entry_time',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='history',
            name='Exit_time',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]
