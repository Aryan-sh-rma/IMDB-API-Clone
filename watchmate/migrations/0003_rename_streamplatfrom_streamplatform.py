# Generated by Django 5.0 on 2023-12-16 10:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('watchmate', '0002_streamplatfrom_watchlist_delete_movie'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='StreamPlatfrom',
            new_name='StreamPlatform',
        ),
    ]
