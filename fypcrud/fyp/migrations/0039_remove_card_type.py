# Generated by Django 4.0.6 on 2022-07-24 20:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fyp', '0038_card_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='type',
        ),
    ]