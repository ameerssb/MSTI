# Generated by Django 4.1.3 on 2022-12-03 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0013_rename_address_contact_address_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='image',
            field=models.ImageField(blank=True, upload_to='about_images/'),
        ),
    ]
