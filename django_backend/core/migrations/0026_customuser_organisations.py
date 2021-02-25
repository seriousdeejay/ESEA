# Generated by Django 3.1.6 on 2021-02-23 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0025_auto_20210223_1428'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='organisations',
            field=models.ManyToManyField(through='core.UserOrganisation', to='core.Organisation'),
        ),
    ]