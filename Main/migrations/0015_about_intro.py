# Generated by Django 4.1.3 on 2022-12-03 14:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0014_about_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='intro',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
