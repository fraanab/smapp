# Generated by Django 4.1.5 on 2023-01-14 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_profile_pfp_alter_profile_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='slug',
            field=models.SlugField(default='<django.db.models.query_utils.DeferredAttribute object at 0x000001F494347EB0>', max_length=255),
        ),
    ]