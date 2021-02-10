# Generated by Django 3.1.6 on 2021-02-10 17:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_auto_20210210_1742'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='parent_topic',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_topics', to='core.topic'),
        ),
    ]
