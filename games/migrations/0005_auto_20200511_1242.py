# Generated by Django 3.0.6 on 2020-05-11 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0004_auto_20200511_1238'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gamesimage',
            old_name='games',
            new_name='game_id',
        ),
    ]
