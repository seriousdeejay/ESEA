# Generated by Django 3.1.6 on 2021-03-14 23:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210314_1818'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='organisation',
            options={'verbose_name': 'organisation', 'verbose_name_plural': 'organisations'},
        ),
        migrations.RenameField(
            model_name='organisation',
            old_name='creator',
            new_name='created_by',
        ),
    ]