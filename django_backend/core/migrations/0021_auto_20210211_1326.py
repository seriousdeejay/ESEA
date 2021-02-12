# Generated by Django 3.1.6 on 2021-02-11 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_topic_parent_topic'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='directindicator',
            options={'verbose_name': 'direct_indicator', 'verbose_name_plural': 'direct_indicators'},
        ),
        migrations.AddField(
            model_name='directindicator',
            name='key',
            field=models.CharField(default='defaultfornow', max_length=45),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='directindicator',
            name='max_number',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='directindicator',
            name='min_number',
            field=models.IntegerField(null=True),
        ),
    ]
