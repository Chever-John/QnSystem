# Generated by Django 3.0 on 2021-08-25 23:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Qn', '0002_auto_20210825_2251'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='survey',
            name='begin_time',
        ),
    ]