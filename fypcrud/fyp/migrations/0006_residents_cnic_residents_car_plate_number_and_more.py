# Generated by Django 4.0.5 on 2022-06-18 13:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fyp', '0005_guests_cnic_guests_car_plate_number_guests_card_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='residents',
            name='CNIC',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='residents',
            name='Car_Plate_Number',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='fyp.car'),
        ),
        migrations.AddField(
            model_name='residents',
            name='Card_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='fyp.card'),
        ),
        migrations.AddField(
            model_name='residents',
            name='Name',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='residents',
            name='Phone_Number',
            field=models.BigIntegerField(null=True),
        ),
    ]
