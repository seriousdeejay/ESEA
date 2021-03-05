# Generated by Django 3.1.6 on 2021-03-05 20:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20210305_1404'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='organisations',
            field=models.ManyToManyField(through='core.UserOrganisation', to='core.Organisation'),
        ),
        migrations.AlterField(
            model_name='method',
            name='organisations',
            field=models.ManyToManyField(blank=True, related_name='methods', to='core.Organisation'),
        ),
        migrations.AlterField(
            model_name='userorganisation',
            name='organisation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='organisations', to='core.organisation'),
        ),
        migrations.AlterField(
            model_name='userorganisation',
            name='participant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participants', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='SurveyResponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(blank=True, max_length=128, null=True)),
                ('finished', models.BooleanField(default=False)),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.survey')),
                ('user_organisation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='survey_responses', to='core.userorganisation')),
            ],
            options={
                'verbose_name': 'survey_response',
                'verbose_name_plural': 'survey_responses',
            },
        ),
        migrations.CreateModel(
            name='QuestionResponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direct_indicator_id', models.IntegerField()),
                ('value', models.TextField()),
                ('survey_response', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question_responses', to='core.surveyresponse')),
            ],
            options={
                'verbose_name': 'question_response',
                'verbose_name_plural': 'question_responses',
            },
        ),
    ]