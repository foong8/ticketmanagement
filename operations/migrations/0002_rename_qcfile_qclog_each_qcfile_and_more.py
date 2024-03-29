# Generated by Django 4.2.7 on 2023-11-20 01:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('operations', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='qclog',
            old_name='qcfile',
            new_name='each_qcfile',
        ),
        migrations.RemoveField(
            model_name='qclog',
            name='requester',
        ),
        migrations.RemoveField(
            model_name='qclog',
            name='role_1',
        ),
        migrations.RemoveField(
            model_name='qclog',
            name='role_2',
        ),
        migrations.AddField(
            model_name='qclog',
            name='mistaked_made_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_qclog', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='qclog',
            name='status',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.CreateModel(
            name='QCticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_1', models.CharField(choices=[('Actual', 'Actual'), ('Shadow_1', 'Shadow_1'), ('Shadow_2', 'Shadow_2'), ('Shadow_3', 'Shadow_3'), ('Shadow_test', 'Shadow_test')], default='Actual', max_length=255)),
                ('role_2', models.CharField(choices=[('Actual', 'Actual'), ('Shadow_1', 'Shadow_1'), ('Shadow_2', 'Shadow_2'), ('Shadow_3', 'Shadow_3'), ('Shadow_test', 'Shadow_test')], default='Shadow_1', max_length=255)),
                ('qcfile', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('attribute_one', models.CharField(blank=True, max_length=255, null=True)),
                ('attribute_two', models.CharField(blank=True, max_length=255, null=True)),
                ('attribute_three', models.CharField(blank=True, max_length=255, null=True)),
                ('attribute_four', models.CharField(blank=True, max_length=255, null=True)),
                ('attribute_five', models.CharField(blank=True, max_length=255, null=True)),
                ('requester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requester', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='qclog',
            name='qcticket',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='qcticket', to='operations.qcticket'),
        ),
    ]
