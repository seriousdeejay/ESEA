# Generated by Django 3.1.6 on 2021-03-02 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20210302_1708'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='options',
            field=models.ManyToManyField(blank=True, related_name='ooo', to='core.QuestionOption'),
        ),
    ]