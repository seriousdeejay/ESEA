# Generated by Django 3.1.6 on 2021-03-09 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_auto_20210306_0017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey',
            name='description',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
    ]
