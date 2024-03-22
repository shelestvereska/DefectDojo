# Generated by Django 4.1.13 on 2024-02-11 15:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo', '0203_alter_dojo_group_social_provider'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='finding',
            options={'ordering': ('numerical_severity', '-date', 'title', 'epss_score', 'epss_percentile')},
        ),
        migrations.AddField(
            model_name='finding',
            name='epss_percentile',
            field=models.FloatField(blank=True, default=None, help_text='EPSS percentile for the CVE. Describes how many CVEs are scored at or below this one.', null=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1.0)], verbose_name='EPSS percentile'),
        ),
        migrations.AddField(
            model_name='finding',
            name='epss_score',
            field=models.FloatField(blank=True, default=None, help_text='EPSS score for the CVE. Describes how likely it is the vulnerability will be exploited in the next 30 days.', null=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1.0)], verbose_name='EPSS Score'),
        ),
        migrations.AddIndex(
            model_name='finding',
            index=models.Index(fields=['epss_score'], name='dojo_findin_epss_sc_e40540_idx'),
        ),
        migrations.AddIndex(
            model_name='finding',
            index=models.Index(fields=['epss_percentile'], name='dojo_findin_epss_pe_567499_idx'),
        ),
    ]
