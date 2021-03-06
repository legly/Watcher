# Generated by Django 3.1.3 on 2020-11-23 18:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dns_finder', '0004_subscriber'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dnsmonitored',
            options={'ordering': ['domain_name'], 'verbose_name': 'Corporate DNS', 'verbose_name_plural': 'Corporate DNS Assets Monitored'},
        ),
        migrations.AlterModelOptions(
            name='dnstwisted',
            options={'ordering': ['-created_at'], 'verbose_name': 'Twisted DNS', 'verbose_name_plural': 'Twisted DNS'},
        ),
    ]
