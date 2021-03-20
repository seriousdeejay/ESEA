# Generated by Django 3.1.6 on 2021-03-19 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20210315_0128'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='uniquetoken',
            field=models.CharField(blank=True, max_length=8),
        ),
        migrations.AlterField(
            model_name='surveyresponse',
            name='survey',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='responses', to='core.survey'),
        ),
    ]