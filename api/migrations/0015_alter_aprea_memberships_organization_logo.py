# Generated by Django 4.1 on 2022-10-24 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_aprea_memberships_organization_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aprea_memberships',
            name='organization_logo',
            field=models.ImageField(blank=True, upload_to='organization_logo/'),
        ),
    ]