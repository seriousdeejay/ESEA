# Generated by Django 3.1.6 on 2021-03-09 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_auto_20210309_1441'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='method',
            name='organisations',
        ),
        migrations.AddField(
            model_name='method',
            name='networks',
            field=models.ManyToManyField(blank=True, related_name='methods', to='core.Network'),
        ),
        migrations.AlterField(
            model_name='survey',
            name='questions',
            field=models.ManyToManyField(to='core.DirectIndicator'),
        ),
    ]
