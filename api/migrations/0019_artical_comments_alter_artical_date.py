# Generated by Django 4.1 on 2022-11-16 06:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_license_company_license_person_alter_artical_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='artical_comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artical_id', models.IntegerField()),
                ('user_name', models.CharField(max_length=54)),
                ('email', models.EmailField(max_length=254)),
                ('user_image', models.CharField(blank=True, max_length=9999999)),
                ('comment', models.CharField(max_length=98765)),
                ('date', models.DateField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='artical',
            name='date',
            field=models.CharField(default=datetime.date(2022, 11, 16), max_length=64),
        ),
    ]
