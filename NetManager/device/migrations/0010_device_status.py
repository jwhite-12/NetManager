# Generated by Django 3.1.5 on 2021-02-15 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0009_remove_device_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
