# Generated by Django 3.1.7 on 2021-04-16 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('time_team', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('code', models.CharField(max_length=120)),
                ('status', models.CharField(choices=[('invited', 'Invited'), ('accepted', 'Accepted')], default='invited', max_length=120)),
                ('date_sent', models.DateTimeField(auto_now_add=True)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invitations', to='time_team.team')),
            ],
        ),
    ]
