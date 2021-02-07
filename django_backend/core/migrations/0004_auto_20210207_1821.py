# Generated by Django 3.1.6 on 2021-02-07 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_post_owner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'organisation', 'verbose_name_plural': 'organisations'},
        ),
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.TextField(default=2, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='name',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
