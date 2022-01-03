# Generated by Django 3.0 on 2021-08-29 00:49

from django.db import migrations, models
import resources.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageModel',
            fields=[
                ('image_id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('instance', models.ImageField(blank=True, default='', upload_to=resources.models.image_directory_path, verbose_name='图片文件')),
            ],
        ),
        migrations.CreateModel(
            name='VideoModel',
            fields=[
                ('video_id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('instance', models.ImageField(blank=True, default='', upload_to=resources.models.video_directory_path, verbose_name='视频文件')),
            ],
        ),
    ]