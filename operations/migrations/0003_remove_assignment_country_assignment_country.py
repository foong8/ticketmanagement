# Generated by Django 4.2.7 on 2023-11-23 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0002_rename_qcfile_qclog_each_qcfile_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assignment',
            name='country',
        ),
        migrations.AddField(
            model_name='assignment',
            name='country',
            field=models.ManyToManyField(related_name='country', to='operations.country'),
        ),
    ]