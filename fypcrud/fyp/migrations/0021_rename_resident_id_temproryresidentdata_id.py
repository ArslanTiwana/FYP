# Generated by Django 4.0.6 on 2022-07-22 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fyp', '0020_temproryresidentdata_resident_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='temproryresidentdata',
            old_name='Resident_id',
            new_name='id',
        ),
    ]
