# Generated by Django 4.1 on 2022-11-16 06:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_artical_comments_alter_artical_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artical_comments',
            name='user_image',
        ),
    ]
