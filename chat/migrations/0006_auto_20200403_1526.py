# Generated by Django 2.2 on 2020-04-03 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0005_auto_20200330_2233'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='read',
        ),
        migrations.AddField(
            model_name='fchat',
            name='last_msg_single',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='fchat',
            name='time_single',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='fchat',
            name='unread_single',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='group',
            name='last_msg_groups',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='group',
            name='time_groups',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='group',
            name='unread_groups',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='github',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='insta',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='twitter',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
