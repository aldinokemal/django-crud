# Generated by Django 3.0.3 on 2020-02-15 12:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('inventori', '0003_auto_20200215_1127'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventaris',
            name='inv_nomor',
            field=models.CharField(default=datetime.datetime(2020, 2, 15, 12, 44, 16, 646608, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
    ]
