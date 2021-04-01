# Generated by Django 2.2.18 on 2021-03-24 21:48

from django.db import migrations, models

def clean_hosts(apps, schema_editor):
    Endpoint = apps.get_model('dojo', 'Endpoint')
    for endpoint in Endpoint.objects.filter(host__contains=':'):
        parts = endpoint.split(':')
        endpoint.host=parts[0]
        endpoint.port=parts[1]
        endpoint.save()

class Migration(migrations.Migration):

    dependencies = [
        ('dojo', '0085_add_publish_date_cvssv3_score'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='endpoint',
            options={'ordering': ['product', 'host', 'protocol', 'port', 'userinfo', 'path', 'query', 'fragment']},
        ),
        migrations.AddField(
            model_name='endpoint',
            name='userinfo',
            field=models.CharField(blank=True, help_text="User info as 'alice', 'bob', etc.", max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='endpoint',
            name='host',
            field=models.CharField(blank=True, help_text="The host name or IP address. It can not include the port number. For example'127.0.0.1', 'localhost', 'yourdomain.com'.", max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='endpoint',
            name='protocol',
            field=models.CharField(blank=True, help_text="The communication protocol/scheme such as 'http', 'ftp', 'dns', etc.", max_length=10, null=True),
        ),
        migrations.RunPython(clean_hosts)
    ]
