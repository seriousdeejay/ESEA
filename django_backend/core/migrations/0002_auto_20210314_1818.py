# Generated by Django 3.1.6 on 2021-03-14 17:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='organisation',
            options={},
        ),
        migrations.RemoveField(
            model_name='organisation',
            name='participants',
        ),
        migrations.AddField(
            model_name='organisation',
            name='members',
            field=models.ManyToManyField(blank=True, related_name='organisations', through='core.UserOrganisation', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='organisation',
            name='creator',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userorganisation',
            name='organisation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='organisation_members', to='core.organisation'),
        ),
    ]