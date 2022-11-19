# Generated by Django 4.1 on 2022-10-26 05:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_user_is_varified_user_otp_alter_artical_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='firstname',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='lastname',
            new_name='last_name',
        ),
        migrations.AlterField(
            model_name='artical',
            name='date',
            field=models.CharField(default=datetime.date(2022, 10, 26), max_length=64),
        ),
        migrations.AlterField(
            model_name='user',
            name='phonenumber',
            field=models.CharField(blank=True, max_length=110),
        ),
    ]
