# Generated by Django 3.1.7 on 2021-04-10 14:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('time_team', '0001_initial'),
        ('time_task', '0002_taskprimary'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('minutes', models.IntegerField(default=0)),
                ('is_track', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entries', to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entries', to='time_task.projecttask')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entries', to='time_task.taskprimary')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entries', to='time_team.team')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
