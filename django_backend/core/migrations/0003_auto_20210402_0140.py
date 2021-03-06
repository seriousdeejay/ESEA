# Generated by Django 3.1.6 on 2021-04-01 23:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210402_0128'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='surveyresponse',
            name='id',
        ),
        migrations.AlterField(
            model_name='surveyresponse',
            name='respondent',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='response', serialize=False, to='core.respondent'),
        ),
        migrations.AlterField(
            model_name='surveyresponse',
            name='token',
            field=models.CharField(max_length=8),
        ),
    ]
