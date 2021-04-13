# Generated by Django 3.1.6 on 2021-04-13 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_questionresponse_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='image',
            field=models.ImageField(blank=True, default='avatar-default.png', upload_to='network/'),
        ),
        migrations.AlterField(
            model_name='question',
            name='answertype',
            field=models.CharField(choices=[('TEXT', 'text'), ('NUMBER', 'number'), ('RADIO', 'radio'), ('CHECKBOX', 'checkbox'), ('SCALE', 'scale')], default='TEXT', max_length=100),
        ),
    ]
