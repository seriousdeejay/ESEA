# Generated by Django 3.1.6 on 2021-04-02 10:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20210402_0140'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='uniquetoken',
        ),
    ]