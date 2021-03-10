# Generated by Django 3.1.6 on 2021-03-09 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_remove_method_networks'),
    ]

    operations = [
        migrations.AddField(
            model_name='network',
            name='methods',
            field=models.ManyToManyField(blank=True, related_name='networks', to='core.Method'),
        ),
    ]
