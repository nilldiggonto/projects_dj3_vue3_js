# Generated by Django 3.2.4 on 2021-06-06 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('class_belong', models.CharField(max_length=120)),
                ('students', models.ManyToManyField(blank=True, null=True, to='students.Student')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='NormalStudent',
        ),
    ]
