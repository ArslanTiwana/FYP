# Generated by Django 4.0.5 on 2022-12-14 07:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fyp', '0045_guests_guesttype'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='Guest',
        ),
        migrations.AddField(
            model_name='guests',
            name='Card_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='fyp.card'),
        ),
    ]
