# Generated by Django 3.1.6 on 2021-02-07 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_remove_post_creator'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='participant',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]