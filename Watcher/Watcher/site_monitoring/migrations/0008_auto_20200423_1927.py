# Generated by Django 3.0.5 on 2020-04-23 19:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_monitoring', '0007_auto_20200422_2316'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alert',
            old_name='ip',
            new_name='new_ip',
        ),
        migrations.RenameField(
            model_name='alert',
            old_name='ip_second',
            new_name='new_ip_second',
        ),
    ]
