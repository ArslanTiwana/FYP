# Generated by Django 4.0.5 on 2022-12-14 07:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fyp', '0047_remove_temproryresidentdata_car_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='Temproryresident',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='fyp.temproryresidentdata'),
        ),
    ]