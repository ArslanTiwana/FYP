# Generated by Django 4.0.6 on 2022-07-22 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fyp', '0019_temproryresidentdata_delete_temproryresident'),
    ]

    operations = [
        migrations.AddField(
            model_name='temproryresidentdata',
            name='Resident_id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='temproryresidentdata',
            name='Car_Plate_number',
            field=models.CharField(max_length=7),
        ),
    ]
