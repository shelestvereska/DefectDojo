# Generated by Django 3.1.8 on 2021-05-13 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo', '0100_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dojo_group',
            name='users',
            field=models.ManyToManyField(blank=True, to='dojo.Dojo_User'),
        ),
    ]
