# Generated by Django 4.0.6 on 2022-07-24 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fyp', '0034_alter_history_entry_time_alter_history_exit_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='Barcode_id',
            field=models.IntegerField(unique=True),
        ),
    ]
