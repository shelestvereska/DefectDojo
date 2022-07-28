# Generated by Django 3.2.14 on 2022-07-28 13:11
import django.db.models.deletion

from django.db import migrations, models


def save_existing_sla(apps, schema_editor):
    system_settings_model = apps.get_model('dojo', 'System_Settings')

    try:
        system_settings = system_settings_model.objects.get()
        critical = system_settings.sla_critical,
        high = system_settings.sla_high,
        medium = system_settings.sla_medium,
        low = system_settings.sla_low
    except:
        critical = 7
        high = 30
        medium = 90
        low = 120

    sla_config = apps.get_model('dojo', 'SLA_Configuration')
    sla_config.objects.create(name='Default',
                                     description='The Default SLA Configuration. Products not using an explicit SLA Configuration will use this one.',
                                     critical=critical,
                                     high=high,
                                     medium=medium,
                                     low=low)


class Migration(migrations.Migration):
    dependencies = [
        ('dojo', '0164_custom_sla'),
    ]

    operations = [
        migrations.RunPython(save_existing_sla),
        migrations.RemoveField(
            model_name='system_settings',
            name='sla_critical',
        ),
        migrations.RemoveField(
            model_name='system_settings',
            name='sla_high',
        ),
        migrations.RemoveField(
            model_name='system_settings',
            name='sla_low',
        ),
        migrations.RemoveField(
            model_name='system_settings',
            name='sla_medium',
        ),
        migrations.AddField(
            model_name='product',
            name='sla_configuration',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.RESTRICT, related_name='sla_config',
                                    to='dojo.sla_configuration'),
        ),
    ]
