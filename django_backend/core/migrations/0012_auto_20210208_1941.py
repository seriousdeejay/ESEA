# Generated by Django 3.1.6 on 2021-02-08 18:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_network'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='network',
            options={'verbose_name': 'network', 'verbose_name_plural': 'networks'},
        ),
    ]