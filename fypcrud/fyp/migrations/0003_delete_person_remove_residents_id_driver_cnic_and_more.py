# Generated by Django 4.0.5 on 2022-06-18 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fyp', '0002_rename_first_name_person_name_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Person',
        ),
        migrations.RemoveField(
            model_name='residents',
            name='id',
        ),
        migrations.AddField(
            model_name='driver',
            name='CNIC',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='driver',
            name='Name',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='driver',
            name='Phone_Number',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='Card_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='fyp.card'),
        ),
        migrations.AlterField(
            model_name='card',
            name='Car_Plate_number',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='card',
            name='Card_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='driver',
            name='Car_Plate_Number',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='fyp.car'),
        ),
        migrations.AlterField(
            model_name='driver',
            name='Card_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='fyp.card'),
        ),
        migrations.AlterField(
            model_name='driver',
            name='Driver_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='guests',
            name='Address',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='guests',
            name='Guest_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='residents',
            name='Resident_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
