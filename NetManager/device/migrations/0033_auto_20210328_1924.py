# Generated by Django 3.1.5 on 2021-03-28 18:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0032_auto_20210328_1823'),
    ]

    operations = [
        migrations.RenameField(
            model_name='device',
            old_name='deviceName',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='device',
            old_name='deviceType',
            new_name='type',
        ),
        migrations.AlterField(
            model_name='log',
            name='dateTime',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 28, 19, 24, 21, 266281)),
        ),
    ]