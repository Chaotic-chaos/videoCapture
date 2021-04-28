# Generated by Django 3.2 on 2021-04-28 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_path', models.CharField(max_length=200)),
                ('video_name', models.CharField(max_length=200)),
                ('video_summary', models.CharField(max_length=500, null=True)),
            ],
        ),
    ]
