# Generated by Django 4.1 on 2022-10-17 12:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_media_title_media_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artical',
            name='date',
            field=models.CharField(default=datetime.date(2022, 10, 17), max_length=64),
        ),
    ]