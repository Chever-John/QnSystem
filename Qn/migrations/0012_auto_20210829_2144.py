# Generated by Django 3.0 on 2021-08-29 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Qn', '0011_auto_20210828_2329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey',
            name='finished_time',
            field=models.DateTimeField(null=True, verbose_name='结束时间'),
        ),
        migrations.AlterField(
            model_name='survey',
            name='release_time',
            field=models.DateTimeField(null=True, verbose_name='发布时间'),
        ),
    ]