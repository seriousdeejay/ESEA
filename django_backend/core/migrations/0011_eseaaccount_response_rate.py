# Generated by Django 3.1.6 on 2021-04-06 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_eseaaccount_sufficient_responses'),
    ]

    operations = [
        migrations.AddField(
            model_name='eseaaccount',
            name='response_rate',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]
