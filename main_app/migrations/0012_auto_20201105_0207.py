# Generated by Django 3.1.2 on 2020-11-05 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_auto_20201105_0207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='content',
            field=models.TextField(),
        ),
    ]
