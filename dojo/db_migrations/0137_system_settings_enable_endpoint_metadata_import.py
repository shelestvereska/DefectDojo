# Generated by Django 3.1.13 on 2021-12-01 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo', '0136_default_group_help_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='system_settings',
            name='enable_endpoint_metadata_import',
            field=models.BooleanField(default=True, help_text='With this setting turned off, endpoint metadata import will be disabled in the user interface.', verbose_name='Enable Endpoint Metadata Import'),
        ),
    ]
