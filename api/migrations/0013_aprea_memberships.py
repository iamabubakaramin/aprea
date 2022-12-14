# Generated by Django 4.1 on 2022-10-24 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_alter_artical_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aprea_memberships',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_organization', models.CharField(choices=[('Association', 'Association'), ('Union', 'Union'), ('Group', 'Group')], max_length=50)),
                ('organization_name', models.CharField(max_length=400, unique=True)),
                ('province', models.CharField(max_length=400)),
                ('city', models.CharField(max_length=400)),
                ('area', models.CharField(blank=True, max_length=400)),
                ('certificate', models.ImageField(blank=True, upload_to='certifcate/')),
                ('register_with', models.CharField(blank=True, max_length=100)),
                ('formed_through', models.CharField(blank=True, choices=[('Elections', 'Elections'), ('By will', 'By will'), ('Other', 'Other')], max_length=100)),
                ('registerd_voters', models.IntegerField(default=0)),
                ('total_agents', models.IntegerField(default=0)),
                ('focal_person_name', models.CharField(blank=True, max_length=100)),
                ('focal_person_number', models.IntegerField(default=0)),
                ('office_address', models.CharField(blank=True, max_length=5000)),
                ('nearest_landmark', models.CharField(blank=True, max_length=5000)),
                ('website', models.URLField(blank=True)),
                ('social_media_url', models.URLField(blank=True)),
                ('a_member_image', models.ImageField(blank=True, upload_to='members/')),
                ('a_cnic_front', models.ImageField(blank=True, upload_to='cnic/')),
                ('a_cnic_back', models.ImageField(blank=True, upload_to='cnic/')),
                ('a_member_type', models.CharField(choices=[('President', 'President'), ('Chairman', 'Chairman'), ('Vice President', 'Vice President'), ('Vice Chairman', 'Vice Chairman'), ('General Secretary', 'General Secretary')], max_length=100)),
                ('a_full_name', models.CharField(max_length=254)),
                ('a_cnic', models.IntegerField(default=0)),
                ('a_date_of_issue', models.DateField(default=0)),
                ('a_busniess_name', models.CharField(blank=True, max_length=250)),
                ('a_email', models.EmailField(blank=True, max_length=254)),
                ('a_contact_number', models.IntegerField(default=0)),
                ('a_busniess_address', models.CharField(blank=True, max_length=5000)),
                ('b_member_image', models.ImageField(blank=True, upload_to='members/')),
                ('b_cnic_front', models.ImageField(blank=True, upload_to='cnic/')),
                ('b_cnic_back', models.ImageField(blank=True, upload_to='cnic/')),
                ('b_member_type', models.CharField(choices=[('President', 'President'), ('Chairman', 'Chairman'), ('Vice President', 'Vice President'), ('Vice Chairman', 'Vice Chairman'), ('General Secretary', 'General Secretary')], max_length=100)),
                ('b_full_name', models.CharField(max_length=254)),
                ('b_cnic', models.IntegerField(default=0)),
                ('b_date_of_issue', models.DateField(default=0)),
                ('b_busniess_name', models.CharField(blank=True, max_length=250)),
                ('b_email', models.EmailField(blank=True, max_length=254)),
                ('b_contact_number', models.IntegerField(default=0)),
                ('b_busniess_address', models.CharField(blank=True, max_length=5000)),
                ('c_member_image', models.ImageField(blank=True, upload_to='members/')),
                ('c_cnic_front', models.ImageField(blank=True, upload_to='cnic/')),
                ('c_cnic_back', models.ImageField(blank=True, upload_to='cnic/')),
                ('c_member_type', models.CharField(choices=[('President', 'President'), ('Chairman', 'Chairman'), ('Vice President', 'Vice President'), ('Vice Chairman', 'Vice Chairman'), ('General Secretary', 'General Secretary')], max_length=100)),
                ('c_full_name', models.CharField(max_length=254)),
                ('c_cnic', models.IntegerField(default=0)),
                ('c_date_of_issue', models.DateField(default=0)),
                ('c_busniess_name', models.CharField(blank=True, max_length=250)),
                ('c_email', models.EmailField(blank=True, max_length=254)),
                ('c_contact_number', models.IntegerField(default=0)),
                ('c_busniess_address', models.CharField(blank=True, max_length=5000)),
            ],
        ),
    ]
