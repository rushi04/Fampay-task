# Generated by Django 3.1.4 on 2020-12-11 23:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Fetch_Video', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='channelId',
        ),
        migrations.AddField(
            model_name='video',
            name='channel_Id',
            field=models.ForeignKey(default='sfsf', on_delete=django.db.models.deletion.CASCADE, related_name='channel_Id', to='Fetch_Video.channel'),
        ),
    ]
