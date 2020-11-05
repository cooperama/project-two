# Generated by Django 3.1.2 on 2020-11-05 09:56

from django.db import migrations, models
import pyuploadcare.dj.models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0012_auto_20201105_0207'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('photo', pyuploadcare.dj.models.ImageField()),
            ],
        ),
    ]
