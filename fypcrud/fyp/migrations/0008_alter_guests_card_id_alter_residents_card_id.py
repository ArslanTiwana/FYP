# Generated by Django 4.0.5 on 2022-06-18 14:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fyp', '0007_alter_guests_card_id_alter_guests_entry_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guests',
            name='Card_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='fyp.card'),
        ),
        migrations.AlterField(
            model_name='residents',
            name='Card_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='fyp.card'),
        ),
    ]