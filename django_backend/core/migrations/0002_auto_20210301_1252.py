# Generated by Django 3.1.6 on 2021-03-01 11:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isMandatory', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('answertype', models.CharField(choices=[('TEXT', 'text'), ('NUMBER', 'number'), ('RADIO', 'radio'), ('CHECKBOX', 'checkbox')], default='TEXT', max_length=100)),
            ],
            options={
                'verbose_name': 'question',
                'verbose_name_plural': 'questions',
            },
        ),
        migrations.AlterField(
            model_name='topic',
            name='parent_topic',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_topics', to='core.topic'),
        ),
    ]
