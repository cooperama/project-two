# Generated by Django 3.1.2 on 2020-11-04 19:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_merge_20201102_2340'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=85)),
                ('country', models.CharField(max_length=85)),
                ('region', models.CharField(max_length=85)),
            ],
        ),
        migrations.AddField(
            model_name='posts',
            name='city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.city'),
        ),
    ]
