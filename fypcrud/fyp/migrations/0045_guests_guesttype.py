# Generated by Django 4.0.5 on 2022-12-14 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fyp', '0044_admin_email_guests_email_residents_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='guests',
            name='GuestType',
            field=models.CharField(default='OneTime', max_length=20),
        ),
    ]
